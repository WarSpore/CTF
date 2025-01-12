from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Util.strxor import strxor
from pwn import xor
import os

key = bytes.fromhex("40f16d6ccbbd071540f16d6ccbbd0715")

def get_cookie():    
    iv = os.urandom(16) 
    message = b"admin=False; username=admin; email=test@example.local"
    message = pad(message, AES.block_size)

    cipher = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(message)
    return iv.hex() + ciphertext.hex()

def check(msg):
    msg = bytes.fromhex(msg)
    iv = msg[0:16]
    print(iv)
    ciphertext = msg[16:]

    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted = cipher.decrypt(ciphertext)
    unpadded = unpad(decrypted, 16)
    print(unpadded)

    if b"admin=True" in unpadded.split(b";"):
        print("! du greide det!")
    else:
        print("du er ikke admin")    

cookie = get_cookie()

iv = (bytes.fromhex(cookie[0:32]))
current = b"admin=False; use"
forged = b"admin=True; user"
msg = xor(xor(iv,current),forged)
cookie = msg.hex()+cookie[32:]

check(cookie)