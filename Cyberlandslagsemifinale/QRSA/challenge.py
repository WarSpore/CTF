from Crypto.Util.number import bytes_to_long, getPrime
from sage.all import QuaternionAlgebra, Zmod
from secret import FLAG, gen_hint
import os


NBITS = 1024


def gen_primes(coeffs, nbits=512):
    a, b, c, d = coeffs
    p, q = getPrime(nbits), getPrime(nbits)
    while pow(b**2 + c**2 - d**2, (p - 1) // 2, p) != 1:
        p = getPrime(nbits)
    while pow(b**2 + c**2 - d**2, (q - 1) // 2, q) != 1:
        q = getPrime(nbits)
    return p, q


a = bytes_to_long(FLAG + os.urandom(NBITS // 8 - len(FLAG) - 1))
assert NBITS // 2 < a.bit_length() < NBITS

b, c, d = [bytes_to_long(os.urandom(NBITS // 8)) for _ in range(3)]

p, q = gen_primes((a, b, c, d), NBITS // 2)
n = p * q
e = 0x10001

# Quaternion algebra over the ring of integers modulo n, i^2 = 1 and j^2 = 1
Q = QuaternionAlgebra(Zmod(n), 1, 1)
i, j, k = Q.gens()
m = a + b*i + c*j + d*k
ct = m**e

A1, B1, C1, A2, B2, C2 = gen_hint(ct, p, q)
assert A1 * B1 * C1 == A2 * B2 * C2 == ct

with open("output.txt", "w") as fout:
    fout.write(f"{n = }\n")
    fout.write(f"{e = }\n")
    fout.write(f"{ct = }\n")

    fout.write(f"{A1 = }\n")
    fout.write(f"{B1 = }\n")
    fout.write(f"{C1 = }\n")

    fout.write(f"{A2 = }\n")
    fout.write(f"{B2 = }\n")
    fout.write(f"{C2 = }\n")
