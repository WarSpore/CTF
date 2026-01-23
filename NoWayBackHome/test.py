from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from hashlib import sha256
from Crypto.Util.number import getPrime, GCD, bytes_to_long, long_to_bytes, inverse
from random import randint
import math
FLAG = b'crypto{????????????????????????????????}'

p, q = getPrime(512), getPrime(512)
n = p * q

# Alice side
v = (p * randint(1, n)) % n
k_A = randint(1, n)
while GCD(k_A, n) != 1:
    k_A = randint(1, n)
vka = (v * k_A) % n

# Bob side
k_B = randint(1, n)
while GCD(k_B, n) != 1:
    k_B = randint(1, n)
vkakb = (vka * k_B) % n

# Alice side
vkb = (vkakb * inverse(k_A, n)) % n

# Bob side
v_s = (vkb * inverse(k_B, n)) % n

print("vka,vkakb:",math.gcd(vka,vkakb))
print("vkb,vkakb:",math.gcd(vkb,vkakb))
print("vka,vkb:",math.gcd(vka,vkb))
print("K_A: ",k_A)
print("K_B: ",k_B)
print("K_V:", v//p)
print("q:",q)
print("p:",p)