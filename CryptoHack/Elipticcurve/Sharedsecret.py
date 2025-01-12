#The shared secret is Q_a = [n_a]G Q_b = [n_b]G S = [n_b]Q_a or S = [n_a]Q_b

'''
def double_and_add(P, n, a, b, p):
    """
    Perform scalar multiplication Q = [n]P using the Double and Add algorithm on an elliptic curve.
    
    Parameters:
        P: tuple (x, y) representing a point on the elliptic curve or 'O' for the point at infinity
        n: integer scalar by which to multiply the point
        a: coefficient of x in the elliptic curve equation y^2 = x^3 + ax + b
        b: constant term in the elliptic curve equation
        p: prime modulus of the finite field
        
    Returns:
        A tuple (x, y) representing the result Q = [n]P, or 'O' for the point at infinity.
    """
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
# Elliptic curve: y^2 = x^3 + 2x + 3 over F_97
a, b, p = 497, 1768, 9739

# Point on the curve
Q = (815,3190)

# Scalar multiplier
n = 1829

# Compute [n]P
result = double_and_add(Q, n, a, b, p)
print(f"[{n}]P =", result)
'''