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

#bare kommuniserte med serveren direkte valgte modus med lavest bit

p = 0xde26ab651b92a129 
g = 0x2
A = 0x96492cf95c2421cb
B = 0x132943fee7fd37c4
iv = "83d6800a712731f72a5d6abe8dab7901"
encrypted_flag = "bc4896640386bb9a9fab156c2959b3615cd29c53e6a40acb33610bab74ef4641"

a = 764947032549944044

shared_secret = pow(B,a,p)

print(decrypt_flag(shared_secret,iv,encrypted_flag))

#script in sage
'''
n=0xde26ab651b92a129
g=0x2
A = 0x4908a8b782b47adf

F = IntegerModRing(n)

a = discrete_log(F(A), F(g))

print(a)

assert F(g)^a == F(A), "Verification failed!"
print("Verification succeeded!")
'''