p = 23
private_key = 5
g = 2
pubkey =(2**5)%p 
s_c2 = 12

def mod_exp(base, exp, modulus):
    return pow(base, exp, modulus)

def find_inverse(x, p):
    # This function finds the modular inverse of x mod p
    return pow(x, p - 2, p)  # Using Fermat's Little Theorem for primes

def recover_message(s_c2, pubkey, private_key, p):
    # s_c2 = s * c2 mod p, pubkey = g^a mod p, private_key = a
    
    # Compute pubkey^{a+k} mod p (this is the factor we need to "cancel")
    factor = mod_exp(pubkey, private_key, p)  # pubkey^a mod p
    
    # Find the inverse of factor mod p
    factor_inv = find_inverse(factor, p)
    
    # Now, multiply s_c2 by factor_inv to recover m
    m = (s_c2 * factor_inv) % p
    return m


print(recover_message(s_c2,pubkey,private_key,p))
