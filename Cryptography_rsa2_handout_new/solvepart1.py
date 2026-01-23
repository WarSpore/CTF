from sympy import gcd, factorint
from Crypto.Util.number import inverse

# Input: List of (e, N) pairs
with open ('Cryptography_rsa2_handout_new\output.txt','r') as fil:
    rsa_keys = []
    print("[",end="")
    for line in fil.readlines():
        
        if line.startswith('e'):
            li = [0]*3
            li[0] = int(line.split('=')[1].strip())
        if line.startswith('n'):
            li[1] = int(line.split('=')[1].strip())
        if line.startswith('c'):
            li[2] = int(line.split('=')[1].strip())
            print(int(line.split('=')[1].strip()),end=",")
        rsa_keys.append(li)
    print("]",end="")
# print(rsa_keys)
cs = []
for tup in rsa_keys:
    cs.append(tup[2])
# print(cs)
# Output list to store weak keys
# weak_keys = []

# def compute_phi(N):
#     """ Factorize N and compute phi(N) for any number of prime factors. """
#     factors = factorint(N)  # Returns {p1: exp1, p2: exp2, ...}
#     phi = 1
#     for p, exp in factors.items():
#         phi *= (p - 1) * (p ** (exp - 1))
#     return phi, factors

# # Process each RSA key pair
# for idx, (e, N) in enumerate(rsa_keys[0:2]):
#     try:
#         phi_N, factors = compute_phi(N)  # Get phi(N) and its prime factors
#         g = gcd(e, phi_N)  # Compute gcd(e, phi(N))

#         if g == 1:
#             d = inverse(e, phi_N)  # Compute d if invertible
#             print(f"Key {idx}: OK (e is invertible)")
#         else:
#             print(f"Key {idx}: WEAK! gcd(e, phi(N)) = {g}, decryption may fail")
#             weak_keys.append((idx, e, N, g, factors))

#     except Exception as err:
#         print(f"Key {idx}: ERROR - {err}")

# # Output weak keys for further analysis
# if weak_keys:
#     print("\nWeak RSA keys detected:")
#     for idx, e, N, g, factors in weak_keys:
#         print(f"Key {idx}: e={e}, N={N}, gcd(e, phi(N))={g}, factors={factors}")
# else:
#     print("\nAll keys seem secure (e was invertible for all).")
