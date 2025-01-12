'''
def point_addition(P, Q, a, b, p):
    """
    Perform point addition on an elliptic curve y^2 = x^3 + ax + b over a finite field F_p.
    
    Parameters:
        P: tuple (x1, y1) or 'O' for the point at infinity
        Q: tuple (x2, y2) or 'O' for the point at infinity
        a: coefficient of x in the elliptic curve equation
        b: constant term in the elliptic curve equation
        p: prime modulus of the finite field
        
    Returns:
        A tuple (x3, y3) representing P + Q, or 'O' for the point at infinity.
    """
    # Case (a): P = O (point at infinity)
    if P == 'O':
        return Q  # P + Q = Q
    
    # Case (b): Q = O (point at infinity)
    if Q == 'O':
        return P  # P + Q = P
    
    # Case (c): Extract coordinates of P and Q
    x1, y1 = P
    x2, y2 = Q
    
    # Case (d): If x1 == x2 and y1 == -y2 (mod p), then P + Q = O
    if x1 == x2 and (y1 + y2) % p == 0:
        return 'O'  # P + Q = O (point at infinity)
    
    # Case (e): Compute the slope λ
    if P != Q:  # Case (e1): P != Q
        numerator = (y2 - y1) % p
        denominator = (x2 - x1) % p
        lam = (numerator * inverse_mod(denominator, p)) % p
    else:  # Case (e2): P == Q
        numerator = (3 * x1^2 + a) % p
        denominator = (2 * y1) % p
        lam = (numerator * inverse_mod(denominator, p)) % p
    
    # Case (f): Compute x3
    x3 = (lam^2 - x1 - x2) % p
    
    # Case (h): Compute y3
    y3 = (lam * (x1 - x3) - y1) % p
    
    # Case (i): Return the result
    return (x3, y3)

# Example Usage:
# Elliptic curve: y^2 = x^3 + 2x + 3 over F_97
a, b, p = 497, 1768, 9739

# Points on the curve
P = (493,5564)
Q = (1539,4742)
R = (4403,5202)
# Compute P + Q

D = point_addition(P, P, a, b, p)
S = point_addition(Q, R, a, b, p)
res = point_addition(D, S, a, b, p)

print("P + P + Q + R =", res)
'''