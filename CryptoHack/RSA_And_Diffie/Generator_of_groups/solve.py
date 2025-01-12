from sympy import mod_inverse, isprime, primerange, factorint

# Parameters
p = 28151
p_minus_1 = p - 1

# Factorization of p-1
factors = factorint(p_minus_1)

# Check if g is primitive
def is_primitive_element(g, p, factors):
    for factor in factors.keys():
        exp = p_minus_1 // factor
        if pow(g, exp, p) == 1:
            return False
    return True

# Find the smallest primitive element
smallest_primitive = None
for g in range(2, p):  # Start from 2 and test each integer
    if is_primitive_element(g, p, factors):
        smallest_primitive = g
        break

print(smallest_primitive,factors)