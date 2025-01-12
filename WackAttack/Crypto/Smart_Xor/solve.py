from pwn import *
from Crypto.Util.number import bytes_to_long, long_to_bytes
from base64 import b64decode, b64encode

r = remote("ctf.wackattack.eu", 5008)
r.recvuntil(b"I just made this XORacle, I can show you how it works by encrypting a flag\nct: ")
cflag = r.recvline()
print(cflag)
decoded_payload = b64decode(cflag)
print(len(decoded_payload))
for byte_value in range(256):
    modified_payload = b64encode(bytes([byte_value+i % 256 for i in range(len(decoded_payload))]))
    r.recvuntil(b"If you want to encrypt anything, encrypt it here")
    r.sendline((modified_payload))
    a = r.recvline()
    response = r.recvline()
    if response == b'>No flag for you\n':
        continue
    print(response)
    if response == b'>No key for you\n':
        continue
    print(modified_payload,response)

    