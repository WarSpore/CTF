'''
def double_and_add_with_y_from_x(x, n, a, b, p):
    """
    Perform scalar multiplication [n]P for an elliptic curve y^2 = x^3 + ax + b (mod p),
    where y is computed from x and p ≡ 3 mod 4.
    
    Parameters:
        x: x-coordinate of the starting point
        n: scalar multiplier
        a: coefficient of x in the elliptic curve equation
        b: constant term in the elliptic curve equation
        p: prime modulus of the finite field (p ≡ 3 mod 4)
        
    Returns:
        A tuple (x, y) representing [n]P.
    """
    def find_y(x, a, b, p):
        """Find y-coordinate given x for y^2 = x^3 + ax + b (mod p) using p ≡ 3 mod 4."""
        rhs = (x^3 + a*x + b) % p  # Compute the right-hand side of the curve equation
        y = power_mod(rhs, (p + 1) // 4, p)  # Compute y = rhs^((p+1)/4) mod p
        if (y^2) % p == rhs:
            return y
        else:
            return p - y  # Return the other square root

    def point_addition(P, Q, a, p):
        """Helper function to add two points on the elliptic curve."""
        if P == 'O':  # P is the point at infinity
            return Q
        if Q == 'O':  # Q is the point at infinity
            return P
        
        x1, y1 = P
        x2, y2 = Q
        
        if x1 == x2 and (y1 + y2) % p == 0:  # P + (-P) = O
            return 'O'
        
        if P != Q:  # Point addition
            lam = ((y2 - y1) * inverse_mod(x2 - x1, p)) % p
        else:  # Point doubling
            lam = ((3 * x1^2 + a) * inverse_mod(2 * y1, p)) % p
        
        x3 = (lam^2 - x1 - x2) % p
        y3 = (lam * (x1 - x3) - y1) % p
        return (x3, y3)
    
    # Compute y-coordinate of P
    y = find_y(x, a, b, p)
    P = (x, y)
    
    # Step 1: Initialize
    Q = P
    R = 'O'  # Start with the point at infinity
    
    # Step 2: Loop while n > 0
    while n > 0:
        # Step 3: Add Q to R if n is odd
        if n % 2 == 1:
            R = point_addition(R, Q, a, p)
        
        # Step 4: Double Q and halve n
        Q = point_addition(Q, Q, a, p)
        n = n // 2
    
    # Step 6: Return the result
    return R

# Example Usage:
# Elliptic curve: y^2 = x^3 + 2x + 3 over F_97, with p ≡ 3 mod 4
a, b, p = 497, 1768,9739

# x-coordinate of the point
x = 4726

# Scalar multiplier
n = 6534

# Compute [n]P
result = double_and_add_with_y_from_x(x, n, a, b, p)
print(f"[{n}]P =", result)
'''