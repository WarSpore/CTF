from Crypto.Util.Padding import pad, unpad
from pwn import *


# Connect to the remote server
r = remote("127.0.0.1", 1337)
# r = remote("challs.glacierctf.com",13374)
def interact_with_server():
    # Step 1: Send option '1' (normal encryption)
    data = r.recv(4096)  # Receive up to 4096 bytes
    print(f"Received raw data: {data}")

    print("Sending option 1...")
    r.sendline(b"1")
    
    # Step 2: Wait for the "Enter plaintext" prompt, then send the payload (plaintext)
    data = r.recv(4096)  # Receive up to 4096 bytes
    print(f"Received raw data: {data}")


    prem = b"premium"
    padded_plaintext = pad(prem, 16)+b"s"
    payload1 = pad(padded_plaintext,16)

    print(f"Sending plaintext: {payload1.decode()}")
    r.sendline(payload1)

    # Step 3: Receive the ciphertext from the server after encryption
    data = r.recvline_contains(b"Ciphertext: ") # Receive up to 4096 bytes
    print(f"Received raw data: {data}")
    
    ct = data.replace(b"Ciphertext: ",b"").strip()
    print(f"Ciphertext received: {ct.decode()}")
    payload2 = ct[0:32]
    data = r.recv(4096)
    r.sendline(b"2")
    print(f"Received raw data: {data}")

    data = r.recv(4096)
    print(f"Server response: {data}")
    print("Sending ct: ")
    r.sendline(payload2)

    data = r.recv(4096)
    print(f"Server response: {data}")
    payload3 = b"qsdlhtl\x08\x08\x08\x08\x08\x08\x08\x08\x08"
    print(f"Sending payload plaintext: {payload3}")
    r.sendline(payload3)
    data = r.recvline_contains(b"Ciphertext: ")
    print(f"Server response: {data}")
    
    ct2 = data.replace(b"Ciphertext: ",b"").strip()
    print("ct2: ",ct2[0:32])
    data = r.recv(4096)
    print(f"Server response: {data}")
    r.interactive()

# Start the interaction with the server
interact_with_server()

# Close the connection
r.close()
