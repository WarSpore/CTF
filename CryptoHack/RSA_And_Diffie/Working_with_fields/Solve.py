def mod_inverse(g, mod):
    """
    Find the modular inverse of g modulo mod using the Extended Euclidean Algorithm.
    """
    # Ensure g is positive and within the modulus
    g = g % mod
    if g == 0:
        raise ValueError("Inverse does not exist because g is zero.")
    
    # Extended Euclidean Algorithm
    t, new_t = 0, 1
    r, new_r = mod, g
    while new_r != 0:
        quotient = r // new_r
        t, new_t = new_t, t - quotient * new_t
        r, new_r = new_r, r - quotient * new_r

    # If r > 1, no modular inverse exists
    if r > 1:
        raise ValueError(f"No modular inverse exists for g = {g} and mod = {mod}.")
    
    # Adjust t to be positive
    if t < 0:
        t = t + mod
    
    return t

# Solve for g * x ≡ 1 mod 991
g = 209
mod = 991
try:
    x = mod_inverse(g, mod)
    print(f"The modular inverse of g = {g} modulo {mod} is x = {x}.")
    # Verify the result
    print(f"Verification: {g} * {x} % {mod} = {(g * x) % mod}")
except ValueError as e:
    print(e)






