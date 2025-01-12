from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad, pad
import os
from pwn import xor



outputfinal = '19a9ab7adc10d9538885835606b4e7b41e19ab2b42bf5b31d033cd31ff7ee481356ec7764d5f5a3acd41cf5aa0110e93540de5a4adcdc1a22e44443b00000004791d206b91e5eb37b40d0ec87a453cb37871dfc95f2e621e22e9bed8197d1254'
outputfinal1 = 'f6d12a8274d7406c2f43d657a3c8b12d61aa0ca3d0647363e06b1bef7dd8a4c430103e0400e979c0f4e8172109217722f6dbe090f838cd2ac6c3d7d2ebe9cbc34a73101ef68d963ebd0407c1734c35ba'
result = xor(bytes.fromhex((outputfinal[128:160])), bytes.fromhex(outputfinal1[128:160]))
print(result)