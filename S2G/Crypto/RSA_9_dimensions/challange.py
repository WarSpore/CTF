from sage.all import *
from Crypto.Util.number import bytes_to_long, isPrime
from random import getrandbits

# Comment: flag.txt includes extra plaintext in addition to the flag
FLAG = open("flag.txt", "rb").read().strip()

e = 65537
print("e =", e)

a = getrandbits(600) | 1
p = getrandbits(400) << 600 | a
while not isPrime(p):
    p = getrandbits(400) << 600 | a
q = getrandbits(400) << 600 | a
while not isPrime(q):
    q = getrandbits(400) << 600 | a

N = p * q
print("N =", N)

e = 65537

flag_chunk_size = len(FLAG) // 9
m = [FLAG[flag_chunk_size * i : flag_chunk_size * (i + 1)] for i in range(9)]
m[-1] = FLAG[flag_chunk_size * 8 :]
m = [bytes_to_long(x) for x in m]

M = matrix(Zmod(N), 3, 3, m)

ct = M**e

print("ct =", list(ct))
