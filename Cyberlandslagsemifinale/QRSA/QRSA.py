from Crypto.Util.number import bytes_to_long, getPrime

b = 5
c = 9
d = 7


for i in range(100):
    p = getPrime(8)
    if pow(b**2 + c**2 - d**2, (p - 1) // 2, p) == 1:
        continue
    print(pow(b**2 + c**2 - d**2, (p - 1) // 2, p))
    print(p)