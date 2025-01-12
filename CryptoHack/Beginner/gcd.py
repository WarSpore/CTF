import numpy as np
def gcd(a,b):
    if a < b:
        a1 = b
        b1 = a
    else:
        a1 = a
        b1 = b
    r = a1%b1
    if r == 0:
        return b1
    return gcd(b1,r)

a = 66528
b = 52920

print(gcd(a,b))