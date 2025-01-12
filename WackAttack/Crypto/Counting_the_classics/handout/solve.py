from Crypto.Util.strxor import strxor
from Crypto.Util.number import long_to_bytes, bytes_to_long
from Crypto.Util.Padding import pad
import secrets
import ast
from collections import Counter

with open ("WackAttack\\Crypto\\Counting_the_classics\\handout\\frequecies") as fil:
    strfreq = fil.read().strip()
    freq = ast.literal_eval(strfreq)





with open ("WackAttack\\Crypto\\Counting_the_classics\\handout\\output","rb") as fil:
    cipher = fil.read().strip()
cipher_blocks = [cipher[i:i+10] for i in range(0, len(cipher), 10)]
new_cipher_blocks = []
for cipher_block in cipher_blocks:
    new_cipher_blocks.append(cipher_block[0:8])
# for cipher_block in new_cipher_blocks:
    # print(hex(bytes_to_long(cipher_block))[2:],end=" ")
key = bytes.fromhex('0e721a4c72171b23')

all_bytes = bytes(range(128))
n = 0
lastbyte = strxor(b"r",bytes([(58+n)%128]))
# print(lastbyte)
k = 0
i = ord('H')
l = 0
w = 0
for cipher_block in cipher_blocks:
    # Convert byte to bytes and concatenate with key
    result = strxor(cipher_block, key + bytes([(88+k)%128])+bytes([(ord('H')+n)%128]))
    n += 1
    l += 1
    if l == 185:
        l = 0
        k += 1
    # Print the result of the XOR operation
    print(result.decode(),end="")