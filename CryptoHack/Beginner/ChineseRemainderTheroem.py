from math import prod

def chinese_remainder_theorem(remainders, moduli):
    """
    Solve a system of congruences using the Chinese Remainder Theorem.
    Arguments:
        remainders: List of remainders [r1, r2, ..., rk].
        moduli: List of moduli [m1, m2, ..., mk].
    Returns:
        The unique solution x modulo the product of the moduli, M = m1 * m2 * ... * mk.
    Raises:
        ValueError: If the moduli are not pairwise coprime.
    """
    if len(remainders) != len(moduli):
        raise ValueError("Lists of remainders and moduli must have the same length.")
    
    # Check if moduli are pairwise coprime
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    
    for i in range(len(moduli)):
        for j in range(i + 1, len(moduli)):
            if gcd(moduli[i], moduli[j]) != 1:
                raise ValueError("Moduli are not pairwise coprime.")
    
    # Compute the product of all moduli
    M = prod(moduli)
    
    # Compute the solution using the formula:
    # x = Σ (remainder_i * Mi * Mi_inverse) mod M
    x = 0
    for i in range(len(moduli)):
        mi = moduli[i]
        Mi = M // mi  # Mi is the product of all moduli except mi
        Mi_inverse = pow(Mi, -1, mi)  # Modular inverse of Mi modulo mi
        x += remainders[i] * Mi * Mi_inverse
    
    # Reduce x modulo M to get the smallest non-negative solution
    return x % M

# Example usage
remainders = [2, 3, 5]
moduli = [5, 11, 17]
try:
    result = chinese_remainder_theorem(remainders, moduli)
    print(f"The solution to the system of congruences is x ≡ {result} (mod {prod(moduli)})")
except ValueError as e:
    print(e)
