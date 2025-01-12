from Crypto.Util.number import bytes_to_long, long_to_bytes
from base64 import b64decode, b64encode
import os
flag = b"A"*30
key = os.urandom(len(flag))
#wack
def encrypt(pt):
    return b64encode(long_to_bytes(bytes_to_long(pt) ^ bytes_to_long(key)))

print("I just made this XORacle, I can show you how it works by encrypting a flag")
print(f"ct: {encrypt(flag).decode()}")
while True:
    print(f"If you want to encrypt anything, encrypt it here")
    inn = input(">")
    inn = b64decode(inn)
    ct = encrypt(inn)
    byte_ct = b64decode(ct)
    if not set(byte_ct).isdisjoint(set(flag)):
        print("No flag for you")
        continue
    if not set(byte_ct).isdisjoint(set(key)):
        print("No key for you")
        continue
    #print(f"ct: {ct.decode()}")
