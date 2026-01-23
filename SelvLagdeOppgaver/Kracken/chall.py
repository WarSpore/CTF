import secrets
import hashlib
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from pwn import xor

class WPA2():
    derived_secret = str(secrets.randbits(128))
    s_nonce = hex(secrets.randbits(128))[2:]
    a_nonce = hex(secrets.randbits(128))[2:]
    replay_counter = 0
    client_ptk = ""
    server_ptk = ""
    packet_number_client = 0
    packet_number_server = 0

    def increment_replay_counter(self):
        self.replay_counter += 1
    
    def decrement_replay_counter(self):
        self.replay_counter -= 1

    def increment_packet_counter_server(self):
        self.packet_number_server += 1
    
    def increment_packet_counter_client(self):
        self.packet_number_client += 1

    def reset_packet_counter_server(self):
        self.packet_number_server = 0
    
    def reset_packet_counter_client(self):
        self.packet_number_client = 0

    def make_payload(self,payload: str):
        return f"{self.replay_counter}_{payload}"
    
    def hash_payload(self, payload: str):
        data = str(self.replay_counter)+payload+self.derived_secret
        hashed = hashlib.sha256(data.encode('utf-8')).hexdigest()
        return hashed
    
    def make_hashed_payload(self,payload: str):
        return f"{self.replay_counter}_{payload}_{self.hash_payload(payload)}"

    def update_client_ptk(self,nonce: str):
        data = self.derived_secret + nonce + self.s_nonce
        self.client_ptk = hashlib.sha256(data.encode('utf-8')).hexdigest()
    
    def update_server_ptk(self,nonce: str):
        data = self.derived_secret + self.a_nonce + nonce
        self.server_ptk = hashlib.sha256(data.encode('utf-8')).hexdigest()
    
    def encrypt_payload(self,payload: str, ptk_key: str, packet_number):
        nonce = pad(str(packet_number).encode(),16)
        hashed = self.hash_payload(nonce.hex()+payload)
        key = bytes.fromhex(ptk_key)[:16]
        cipher = AES.new(key, AES.MODE_ECB)
        keystream = cipher.encrypt(nonce)
        encrypted = xor(keystream,payload.encode("utf-8")).hex()
        return f"{self.replay_counter}_{nonce.hex()+encrypted}_{hashed}"
    
    def decrypt_payload(self,payload: str, ptk_key: str):
        parts = payload.split("_")
        nonce = bytes.fromhex(parts[1][:32])
        key = bytes.fromhex(ptk_key)[:16]
        cipher = AES.new(key, AES.MODE_ECB)
        keystream = cipher.encrypt(nonce)
        decrypted = xor(bytes.fromhex(parts[1][32:]),keystream)
        return f"{self.replay_counter}_{nonce.hex()+(decrypted).decode()}_{parts[2]}"


def menu():
    print("Select an option (1, 2, or 3):")
    print('''
1) Intercept packet
2) Modify packet
3) Do nothing       
          ''')
    choice = input("> ")
    try:
        if choice == "1":
            return choice
        elif choice == "2":
            try:
                return input("Give new packet:")
            except:
                print("Something went wrong")
                menu()
        elif choice == "3":
            return None
    except:
        print("Invalid option")
        menu()

def check_hash(packet: WPA2,payload: str):
    parts = payload.split("_")
    data = parts[0]+parts[1]+packet.derived_secret
    test_hash = hashlib.sha256(data.encode('utf-8')).hexdigest()
    return test_hash == parts[2]
def check_replay_counter(packet: WPA2, replay_counter: int):
    return packet.replay_counter == replay_counter

def first_packet(packet: WPA2):
    payload = packet.make_payload(packet.a_nonce)
    print(f"Server sending ReplayCounter_Anonce: {payload}")
    change = menu()
    if change == "1":
        print(f"Client did not recieve anything")
        payload = None
        return None
    elif change is not None:
        print(f"Client recieved: {change}")
        payload = change
    else:
        print(f"Client recieved: {payload}")
    try:
        parts = payload.split("_")
        nonce = parts[1]
        replay_counter = int(parts[0])
        if not check_replay_counter(packet,replay_counter):
            return None
        packet.update_client_ptk(nonce)
        return 1
    except:
        None
def second_packet(packet: WPA2):
    payload = packet.make_hashed_payload(packet.s_nonce)
    print(f"Client sending ReplayCounter_Snonce_hash: {payload}")
    change = menu()
    if change == "1":
        print(f"Server did not recieve anything")
        return None
    elif change is not None:
        print(f"Server recieved: {change}")
        payload = change
    else:
        print(f"Server recieved: {payload}")
    try:
        parts = payload.split("_")
        nonce = parts[1]
        replay_counter = int(parts[0])
        if not check_replay_counter(packet,replay_counter):
            return None
        check = check_hash(packet,payload)
        if check:
            packet.update_server_ptk(nonce)
        else:
            return None
        return 1
    except:
        return None

def third_packet(packet: WPA2):
    gtk = secrets.token_bytes(16).hex()[:16]
    encrypted_payload = packet.encrypt_payload(gtk,packet.server_ptk,packet.packet_number_server)
    packet.increment_packet_counter_server()
    print(f"Server sending payload xored with keystream from AES ECB mode. Keystream derived from cipher.encrypt(nonce) with session key as key. Format is ReplayCounter_nonce(hex)+encrypted(hex)_hash: {encrypted_payload}")
    change = menu()
    if change == "1":
        print(f"Client did not recieve anything")
        return None
    elif change is not None:
        print(f"Client recieved: {change}")
        encrypted_payload = change
    else:
        print(f"Client recieved: {encrypted_payload}")
    try:
        parts = encrypted_payload.split("_")
        replay_counter = int(parts[0])
        if not check_replay_counter(packet,replay_counter):
            return None
        try:
            decrypted_payload = packet.decrypt_payload(encrypted_payload,packet.client_ptk)
        except:
            return None

        check = check_hash(packet,decrypted_payload)
        if check:
            packet.increment_packet_counter_client()
            return 1
        else:
            return None
    except:
        return None

def fourth_packet(packet: WPA2):
    payload = packet.make_hashed_payload(payload="x")
    print(f"Client sending ReplayCounter_x (Essentially empty payload)_hash: {payload}")
    change = menu()

    if change == "1":
        print(f"Server did not recieve anything")
        return None
    elif change is not None:
        print(f"Server recieved: {change}")
        payload = change
    else:
        print(f"Server recieved: {payload}")
    try:
        parts = payload.split("_")
        replay_counter = int(parts[0])
        if not check_replay_counter(packet,replay_counter):
            return None
        
        check = check_hash(packet,payload)    
        if check:
            return 1
        else:
            return None
    except:
        return None

def fourth_packet_encrypted(packet: WPA2):
    payload = packet.encrypt_payload("x",packet.client_ptk,packet.packet_number_client)
    packet.increment_packet_counter_client()
    print(f"Client sending ReplayCounter_x (Essentially empty payload)_hash: {payload}")
    change = menu()
    if change == "1":
        print(f"Server did not recieve anything")
        return None
    elif change is not None:
        print(f"Server recieved: {change}")
        payload = change
    else:
        print(f"Server recieved: {payload}")
    try: 
        parts = payload.split("_")
        replay_counter = int(parts[0])
        if not check_replay_counter(packet,replay_counter):
            return None
        
        check = check_hash(packet,payload)    
        if check:
            packet.increment_packet_counter_server()
            return 1  
        else:
            return None
    except:
        return None

def flag_packet(packet: WPA2):
    encrypted_payload = packet.encrypt_payload("ctf{KRACKATTACK}",packet.client_ptk,packet.packet_number_client)
    print(f"Client sending flag_packet ReplayCounter_nonce(hex)+encryptedflag(hex)_hash: {encrypted_payload}")
    packet.increment_packet_counter_client()
    change = menu()
    if change == "1":
        print(f"Server did not recieve anything")
        return None
    elif change is not None:
        print(f"Server recieved: {change}")
        encrypted_payload = change
    else:
        print(f"Server recieved: {encrypted_payload}")
    try: 
        parts = encrypted_payload.split("_")
        replay_counter = int(parts[0])
        if not check_replay_counter(packet,replay_counter):
            return None
        check = check_hash(packet,encrypted_payload)    
        if check:
            packet.increment_packet_counter_server()
            return 1
        else:
            return None
    except:
        return None

def main():
    print("Welcome to this WPA2 exchange. Feel free to watch or modify any packet, you will not be able to reveal the flag :)")
    packet = WPA2()
    while True:
        if first_packet(packet) is None:
            continue
        break
    while True:
        if second_packet(packet) is None:
            continue
        break
    packet.increment_replay_counter()
    while True:    
        if third_packet(packet) is None:
            continue
        break
    if fourth_packet(packet) is None:
        packet.increment_replay_counter()
        flag_packet(packet)
        packet.reset_packet_counter_client()
        packet.decrement_replay_counter()
        if third_packet(packet) is None:
            exit(0)
        fourth_packet_encrypted(packet)

    packet.increment_replay_counter()
    flag_packet(packet)
    exit(0)
main()