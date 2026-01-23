from Crypto.Util.number import getPrime, bytes_to_long

n_bits = 1024

flag = b"flag{this_is_a_placeholder}"

p, q = getPrime(n_bits), getPrime(n_bits)
n = p*q
e = 65537

A= matrix([[p,1,0],[q,0,1]])
W = diagonal_matrix([2**(n_bits), 1, 1])

B = (A*W).LLL() / W
r = B[0] if B[0][0] != 0 else B[1]
r *= r[0]

F = Integers(n)

ct = F(bytes_to_long(flag))^e
print(f"{ct=}")
print(f"{e=}")
print(f"a,b = {r[1:]}")