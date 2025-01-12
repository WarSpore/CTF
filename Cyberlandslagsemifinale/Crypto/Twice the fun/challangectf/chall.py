from Crypto.Util.number import getPrime, isPrime, bytes_to_long

flagg = b"flag{fake_flagg}"
e = 65537

p = getPrime(1024)
q = 2*p+1
while not isPrime(q):
    q+=2

n = p*p*q

ct = pow(bytes_to_long(flagg), e, n)

print(f"{n=}")
print(f"{e=}")
print(f"{ct=}")
