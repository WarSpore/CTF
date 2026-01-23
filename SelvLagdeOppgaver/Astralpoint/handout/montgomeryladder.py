from sage.all import *

# ----- x-only Montgomery primitives -----

def montgomery_double(A24, X, Z):
    # (X:Z) -> (X2:Z2) = [2](X:Z)
    A  = X + Z
    AA = A*A
    B  = X - Z
    BB = B*B
    E  = AA - BB
    X2 = AA * BB
    Z2 = E * (BB + A24*E)
    return (X2, Z2)

def montgomery_addition(X1, Z1, X2, Z2, Xdiff, Zdiff):
    # Given (X1:Z1) ~ P, (X2:Z2) ~ Q, and (Xdiff:Zdiff) ~ (Q-P),
    # return (X3:Z3) ~ (P+Q).
    U = (X1 - Z1) * (X2 + Z2)
    V = (X1 + Z1) * (X2 - Z2)
    X3 = Zdiff * (U + V)**2
    Z3 = Xdiff * (U - V)**2
    return (X3, Z3)

# ----- Montgomery ladder -----

def montgomery_ladder(m, A, xP, p):
    """
    Compute x([m]P) on the Montgomery curve By^2 = x^3 + A x^2 + x over F_p (with B=1).
    Inputs:
      m  : nonnegative integer scalar
      A  : curve parameter (int or F_p element)
      xP : affine x-coordinate of base point P (int or F_p element)
      p  : prime modulus
    Returns:
      (X:Z) of [m]P and the affine x (or None if infinity)
    """
    F   = GF(p)
    A   = F(A)
    A24 = (A + 2) / 4
    # Difference point is P itself in the ladder: Q1 - Q0 = P
    Xdiff, Zdiff = F(xP), F(1)

    # Initialize state
    Q0 = (F(1), F(0))        # infinity (1:0)
    Q1 = (Xdiff, Zdiff)      # P = (xP:1)

    bits = bin(int(m))[2:]   # MSB -> LSB
    for b in bits:
        if b == '0':
            # (Q0, Q1) <- ([2]Q0, diffadd(Q0, Q1, P))
            X0,Z0 = Q0
            X1,Z1 = Q1
            Q1 = montgomery_addition(X0, Z0, X1, Z1, Xdiff, Zdiff)
            Q0 = montgomery_double(A24, X0, Z0)
        else:
            # (Q0, Q1) <- (diffadd(Q0, Q1, P), [2]Q1)
            X0,Z0 = Q0
            X1,Z1 = Q1
            Q0 = montgomery_addition(X0, Z0, X1, Z1, Xdiff, Zdiff)
            Q1 = montgomery_double(A24, X1, Z1)

    return Q0[0],Q0[1]
