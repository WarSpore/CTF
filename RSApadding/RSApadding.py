from Crypto.Util.number import bytes_to_long, getPrime
from secrets import token_bytes, randbelow
from math import log2
import os

flag = os.environ.get("FLAG", "wack{flag_for_testing}")
p = getPrime(2048)
q = getPrime(2048)
n = p*q
e = 65537
d = pow(e, -1, (p-1)*(q-1))

def pad(m, n):
    l = int(log2(n)) // 8
    print(l)
    p = token_bytes(l - len(m))
    print(len(p))
    while bytes_to_long(p + m) > n:
        p = token_bytes(l - len(m))
    return p.hex(), bytes_to_long(p + m)

def encrypt(m):
    p, pm = pad(m, n)
    ct = pow(pm, e, n)
    return p, ct

def decrypt(ct):
    p = pow(ct, d, n)
    return p

if __name__ == "__main__":
    secrets = [token_bytes(32) for _ in range(3)]
    numbers = [randbelow(3) for _ in range(100)]
    print(f"Public parameters: {n=} {e=}")
    print("Can you distinguish between the following padded plaintexts")
    for n_i in numbers:
        p, ct = encrypt(secrets[n_i])
        print(f"{p=}\n{ct=}")
    print("Before you answer I will give you a decryption querry")
    print("Input a ciphertext")
    ct = int(input("> "))
    print(f"Here is the result: {decrypt(ct)}")
    print("What are my numbers")
    inn = input("> ") 
    if inn == ",".join(str(i) for i in numbers):
        print(f"Good job here is the flag: {flag}")
    else:
        print("Too bad, that is not correct")

