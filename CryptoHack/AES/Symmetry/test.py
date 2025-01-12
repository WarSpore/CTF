from Crypto.Cipher import AES
import os

KEY = b"a"*16
FLAG ="b"*32

def encrypt(plaintext, iv):
    plaintext = bytes.fromhex(plaintext)
    print(plaintext)
    iv = bytes.fromhex(iv)
    if len(iv) != 16:
        return {"error": "IV length must be 16"}

    cipher = AES.new(KEY, AES.MODE_OFB, iv)
    encrypted = cipher.encrypt(plaintext)
    ciphertext = encrypted.hex()
    
    return {"ciphertext": ciphertext}

def encrypt_flag():
    iv = b"9"*16

    cipher = AES.new(KEY, AES.MODE_OFB, iv)
    encrypted = cipher.encrypt(FLAG.encode())
    ciphertext = iv.hex() + encrypted.hex()
    print(iv.hex())
    return {"ciphertext": ciphertext}

print(encrypt_flag())
print(encrypt("0"*32,"39393939393939393939393939393939"))

ct = "39393939393939393939393939393939eb46b62ea40710e1736bb2045acea10d0944f78327f162bd28b6e70d8ddbbc8b"

p = "b4afd82d32f92c9607bff4e1536dab13"