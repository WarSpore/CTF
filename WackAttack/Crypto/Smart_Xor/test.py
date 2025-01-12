from Crypto.Util.number import bytes_to_long, long_to_bytes
from base64 import b64decode, b64encode
import os

flag = b"wack{dette_er_et_test_flag}"

def encrypt(pt):
    return b64encode(long_to_bytes(bytes_to_long(pt) ^ bytes_to_long(key)))
key = os.urandom(len(flag))
i = -1
while True:
    
    key = os.urandom(len(flag))
    encrypt(flag).decode()
    # print(f"If you want to encrypt anything, encrypt it here")
    inn = "AAAAAAAAAAAAAAAAAAAAAA=="
    inn = b64decode(inn)
    ct = encrypt(inn)
    byte_ct = b64decode(ct)
    print(set(byte_ct),set(flag))
    i += 1
    if not set(byte_ct).isdisjoint(set(flag)):
        print("No flag for you")
        continue
    print(i)
    if not set(byte_ct).isdisjoint(set(key)):
        print("No key for you")
        continue
    print(f"ct: {ct.decode()}")
