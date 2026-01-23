from Crypto.Util.number import bytes_to_long, isPrime, long_to_bytes
import math


def legendre_symbol(a, p):
    """Compute the Legendre symbol (a/p)"""
    return pow(a, (p - 1) // 2, p)

def tonelli_shanks(b, p):
    """Solve x^2 ≡ b mod p using the Tonelli–Shanks algorithm"""
    if legendre_symbol(b, p) != 1:
        return None  # No solution exists

    # Simple cases
    if b == 0:
        return 0
    if p == 2:
        return b

    # p ≡ 3 mod 4 shortcut
    if p % 4 == 3:
        return pow(b, (p + 1) // 4, p)

    # Factor p-1 as Q * 2^S
    S = 0
    Q = p - 1
    while Q % 2 == 0:
        Q //= 2
        S += 1

    # Find a non-residue z
    z = 2
    while legendre_symbol(z, p) != p - 1:
        z += 1

    # Initialization
    M = S
    c = pow(z, Q, p)
    t = pow(b, Q, p)
    R = pow(b, (Q + 1) // 2, p)

    while t != 1:
        # Find the smallest i such that t^(2^i) ≡ 1 mod p
        i = 0
        temp = t
        while temp != 1:
            temp = pow(temp, 2, p)
            i += 1
            if i == M:
                return None  # Shouldn't happen

        # Update values
        b = pow(c, 2 ** (M - i - 1), p)
        M = i
        c = pow(b, 2, p)
        t = (t * c) % p
        R = (R * b) % p
    return R  # One of the square roots. The other is p - R

def linear_congruence(a, b, m):
    from math import gcd

    # Compute gcd and the coefficients x, y such that ax + my = gcd(a, m)
    def extended_gcd(a, b):
        if b == 0:
            return a, 1, 0
        g, x1, y1 = extended_gcd(b, a % b)
        x, y = y1, x1 - (a // b) * y1
        return g, x, y

    g, x, _ = extended_gcd(a, m)

    if b % g != 0:
        return None  # No solution exists

    # Normalize the solution
    x0 = (x * (b // g)) % m
    return x0


E = 65537
c = 42863630919983371044479600495101425468940214748098950614537167230522611852908495061786383505040865371417150544463907816267261982055532001315873021363398743216702192862220197069211177595251116925391267854644446467010011377711743862132034427485091905967226677285863555510908427765699618239596660215305188399467
v = 121456175577805699355742783034180730693470876768350494734173796696025149295453137000302458720761350756664964614548747600275148120468754949990858142346346747097339760652563112840875642815529393201682639904038618104016504154879340903951481300293620691542049214439403638584738259311950262808420504606644081561095
q = 145128210869029541153623250851302298165357388797513222334229309170163385830522939271910551383146034484907190419497707670229373278853595181357038487339240266546279470662587288828567140318144653758756198369925443624414204321852730916392286678634279468595566820994772044680703664599296896345474576977995180372891

b = (pow(1 - v**2 * pow(c, -2, q), -1, q))


rhs = pow(1 - v**2 * pow(c, -2, q), -1, q) % q
gamma_squared = rhs

# Solve x^2 ≡ gamma_squared mod q
gamma = tonelli_shanks(gamma_squared, q) # First root (Andre er riktig)

gamma = q - gamma  # Second root


red = (gamma*c**2)%q

x = linear_congruence(red,E,q)

assert E == gamma * x * c**2 % q

p = E*v*pow(c*c,-1,q)%q


red2 = (gamma*v)%q

y = linear_congruence(red2,p,q)

assert(p == gamma * y * v % q)

print(long_to_bytes(x))
