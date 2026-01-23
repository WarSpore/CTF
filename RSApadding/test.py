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
    p = token_bytes(l - len(m))
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
    numbers = [randbelow(3) for _ in range(2)]
    
    p1, ct1 = encrypt(secrets[0])
    p2, ct2 = encrypt(secrets[1])
    print("p1:",p1,"p2:",p2,"n:",n)
    ct = int(ct1*pow(ct2,-1,n))
    print(f"Here is the result: {decrypt(ct)}")
    print("What are my numbers")
    inn = input("> ") 
    if inn == ",".join(str(i) for i in numbers):
        print(f"Good job here is the flag: {flag}")
    else:
        print("Too bad, that is not correct")

