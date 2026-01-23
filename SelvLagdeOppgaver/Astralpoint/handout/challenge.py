from sage.all import *
from secrets import randbelow
from Crypto.Cipher import AES
from Crypto.Hash import SHA3_256
from Crypto.Util.number import long_to_bytes, bytes_to_long
from montgomeryladder import *
from Crypto.Util.Padding import pad
from secret import get_flag

p = 3753523986167412422789273084260419393543913010317 
Fp = GF(p) 
A = 486662
E = EllipticCurve(Fp, [0, A, 0, 1, 0])

N = E.cardinality()
r, e = max(factor(N))
h = N // r                         
R = E.random_point()
G = h * R

assert e == 1
assert r*G == E(0)

ell = G.order()
secret = randbelow(int(ell))
Qx, Qy = montgomery_ladder(secret, A, G.xy()[0], p)

h_obj = SHA3_256.new()
h_obj.update(long_to_bytes(secret))
key = h_obj.digest()

cipher = AES.new(key, AES.MODE_CBC)
iv = cipher.iv

flag = get_flag()
ciphertext = cipher.encrypt(pad(flag,16))

print("p =", p)
print("ell =" , ell)
print("cofactor = ", h)
print("secret_bin_length = ",len(bin(secret))-2)
print("Px =", G.xy()[0])
print("Py =", G.xy()[1])
print("Qx =", Qx)
print("Qy =", Qy)
print("ct =", hex(bytes_to_long(iv+ciphertext)))
