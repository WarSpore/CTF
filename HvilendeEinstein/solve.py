from Crypto.Util.number import bytes_to_long, long_to_bytes 
import math

E = 65537
c = 5509755028311913693889152989811589325618825721285320623763941739852324692885042997295017302495580876595625754080921065571156707913564253269808788119785744
p = 9074104511432081580600526701050375071012419739731285071631187126305749425747209598708060338457487435389911091745507544857287671744266465012785227600297203
m = 1
c_red = (c**2)%p

def linear_congruence(a, b, m):
    from math import gcd
    def extended_gcd(a, b):
        if b == 0:
            return a, 1, 0
        g, x1, y1 = extended_gcd(b, a % b)
        x, y = y1, x1 - (a // b) * y1
        return g, x, y

    g, x, _ = extended_gcd(a, m)

    if b % g != 0:
        return None
    x0 = (x * (b // g)) % m
    return x0
print(c_red)
sol = (linear_congruence(c_red,E,p))
print(long_to_bytes(sol))