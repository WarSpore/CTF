import os
from typing import List
from Crypto.Util.Padding import pad, unpad
from Crypto.Cipher import AES
from pwn import *

key = b"a"*16
prem = b"premium"
cipher = AES.new(key, AES.MODE_ECB)
padded_plaintext = pad(prem, 16)+b"s"
print(padded_plaintext)
padded_pad = pad(padded_plaintext,16)
print(padded_pad)
# Encrypt the padded plaintext
ciphertext=b""
for i in range(0,len(padded_pad),16):
    ciphertext += cipher.encrypt(padded_pad[i:i+16])
print(ciphertext)
ciphertext = ciphertext[0:16] 
dt = b""
dt += cipher.decrypt(ciphertext[0:16])
print(unpad(dt,16)) 


ct = "367675233d6f89c723aaff70aac26f801b1d629aa323266c0f36b137a4e18f2f"
print(ct[0:32])