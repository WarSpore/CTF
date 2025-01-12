from Crypto.Cipher import AES
import os
from Crypto.Util.Padding import pad, unpad
from datetime import datetime, timedelta
from pwn import *

KEY = b"3"*16
FLAG = "?"

def check_admin(cookie, iv):
    cookie = bytes.fromhex(cookie)
    iv = bytes.fromhex(iv)
    cipher = AES.new(KEY, AES.MODE_CBC, iv)
    decrypted = cipher.decrypt(cookie)
    unpadded = unpad(decrypted, 16)
    print(unpadded)

    if b"admin=True" in unpadded.split(b";"):
        return "flag"
    else:
        return "error"

def get_cookie():
    expires_at = "11111111111"
    cookie = f"admin=False;expiry={expires_at}".encode()

    iv =  b"2"*16
    padded = pad(cookie, 16)
    cipher = AES.new(KEY, AES.MODE_CBC, iv)
    encrypted = cipher.encrypt(padded)
    ciphertext = iv.hex() + encrypted.hex()

    return {"cookie": ciphertext}


ct = "3232323232323232323232323232323230f90b3ac7c7af2032a878fa4c511a486dbebbee952e9a1576bd9ee62b2275fa"
iv = ct[:32]
c1 = ct[16:32]
c2 = ct[32:48]
c = ct[32:]
print(c)
ivmod = (xor(b"admin=False;expi",b"admin=True;expi",bytes.fromhex(iv)).hex())
print((ivmod))
check_admin(c,ivmod)