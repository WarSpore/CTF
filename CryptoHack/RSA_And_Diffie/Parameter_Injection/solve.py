from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Util.number import long_to_bytes, bytes_to_long
import hashlib
from pwn import *
import json

def is_pkcs7_padded(message):
    padding = message[-message[-1]:]
    return all(padding[i] == len(padding) for i in range(0, len(padding)))


def decrypt_flag(shared_secret: int, iv: str, ciphertext: str):
    # Derive AES key from shared secret
    sha1 = hashlib.sha1()
    sha1.update(str(shared_secret).encode('ascii'))
    key = sha1.digest()[:16]
    # Decrypt flag
    ciphertext = bytes.fromhex(ciphertext)
    iv = bytes.fromhex(iv)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext)

    if is_pkcs7_padded(plaintext):
        return unpad(plaintext, 16).decode('ascii')
    else:
        return plaintext.decode('ascii')

r = remote("socket.cryptohack.org",13371)
r.recv()
intercepted_json = r.recvuntil(b"\n")
data = json.loads(intercepted_json)
print(data)

p = int(data["p"], 16)  # The large prime number, converted from hexadecimal to integer
g = int(data["g"], 16)  # The generator (primitive root), converted from hexadecimal to integer
A = int(data["A"], 16)  # Alice's public key, converted from hexadecimal to integer
b = 197395083814907028991785772714920885908249341925650951555219049411298436217190605190824934787336279228785809783531814507661385111220639329358048196339626065676869119737979175531770768861808581110311903548567424039264485661330995221907803300824165469977099494284722831845653985392791480264712091293580274947132480402319812110462641143884577706335859190668240694680261160210609506891842793868297672619625924001403035676872189455767944077542198064499486164431451944
Amod = "0x01"


# Now create the JSON object to send to Bob (or the server)
payload_json = {
    "p" : hex(p),
    "g" : hex(g),
    "A" : Amod
}

# Convert the payload into a JSON string
payload_json_str = json.dumps(payload_json)
r.sendline(payload_json_str)
r.recv()
r.recv()
intercepted_json = r.recvuntil(b"\n")
data = json.loads(intercepted_json)
print(data)

B = data["B"]

Bmod = "0x01"

payload_json = {
    "B" : Bmod
}
payload_json_str = json.dumps(payload_json)
r.sendline(payload_json_str)
r.recv()
intercepted_json = r.recvuntil(b"\n")

intercepted_json = intercepted_json.replace(b"Intercepted from Alice: ",b"")
data = json.loads(intercepted_json.strip())
print(data)
shared_secret = pow(int(Amod,16), 11, p)
iv = data["iv"]  # The large prime number, converted from hexadecimal to integer
encrypted_flag = data["encrypted_flag"] # The generator (primitive root), converted from hexadecimal to integer
print(decrypt_flag(shared_secret,iv,encrypted_flag))
r.close()