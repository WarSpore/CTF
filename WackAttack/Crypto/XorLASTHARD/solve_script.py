from pwn import *
from Crypto.Util.number import bytes_to_long, long_to_bytes
from base64 import b64decode, b64encode
while True:
    r = remote("ctf.wackattack.eu", 5009)
    r.recvuntil(b"I just made this XORacle, I can show you how it works by encrypting a flag\nct: ")
    cflag = r.recvline()
    print(cflag)
    decoded_payload = b64decode(cflag)
    r.recvuntil(b"If you want to encrypt anything, encrypt it here")
    r.sendline(b"AAAAAAAAAAAAAAAAAAAAAA==")
    a = r.recvline()
    response = r.recvline()
    if response != b'>No flag for you\n':
        print(response)
        break
    r.close()

for byte_value in range(256):
    modified_payload = b64encode(bytes([(byte_value+i) % 256 for i in range(len(decoded_payload))]))
    r.recvuntil(b"If you want to encrypt anything, encrypt it here")
    r.sendline((modified_payload))
    a = r.recvline()
    response = r.recvline()
    if response == b'>No flag for you\n':
        continue
    if response == b'>No key for you\n':
        continue
    print("modified_payload",modified_payload)
    payload = modified_payload
    r.sendline(payload)
    break

first_byte_key = xor(decoded_payload[:1],b"w")


key = []
for byte_value in range(256):
    test_byte = bytes([byte_value])
    modified_payload2 = b64encode(test_byte+b64decode(payload)[1:])
    r.recvuntil(b'If you want to encrypt anything, encrypt it here\n')
    r.sendline(modified_payload2)
    response = r.recvline()
    if response == b'>No flag for you\n':
        continue
    if response == b'>No key for you\n':
        key.append(xor(test_byte,first_byte_key))
    if response == b'>If you want to encrypt anything, encrypt it here\n':
        r.sendline(modified_payload2)
        
    
print(cflag,key)
r.close()
    