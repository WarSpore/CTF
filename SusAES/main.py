#!/usr/bin/env python3

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import os

key = os.urandom(16)

def decrypt(ct: bytes, key: bytes) -> str:
    c = AES.new(key, AES.MODE_ECB)
    return c.decrypt(ct).hex()

def encrypt_flag(flag: str, key: bytes) -> str:
    iv = os.urandom(16)

    c = AES.new(key, AES.MODE_CBC, iv)
    enc = c.encrypt(pad(flag.encode(), 16))
    return iv.hex() + enc.hex()

while True:
    print('\nMenu:\n\t1: decrypt msg\n\t2: print encrypted flag')
    inp = int(input())
    
    if inp == 1:
        inp = input('Enter ciphertext: ')
        print(f'Decrypted: {decrypt(bytes.fromhex(inp), key)}')

    if inp == 2:
        print(f'Here is encrypted flag: {encrypt_flag("flag", key)}')