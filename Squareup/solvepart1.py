from math import gcd
from Crypto.Util.number import long_to_bytes, bytes_to_long, inverse

# ------------------------------------------------------------------
# public data from the challenge
N = 1298690852855676717877172430649235439701166577296380685015744142960768447038281361897617173145966407353660262643273693068083328108519398663073368426744653753236312330497119252304579628565448615356293308415969827357877088267274695333

c = 162345251908758036296170413099695514860545515965805244415511843227313118622229046299657295062100889503276740904118647336251473821440423216697485906153356736210597508871299190718706584361947325513349221296586217139380060755033205077

lp, lq = 1, -1                     # Legendre bits that came with c

# the *buggy* decrypt output that was printed for you
m_tilde_hex = (
    "1b5220c4f08fa76ca4ddbff733f3e928c851ddbd2c08bd7faf6d9bbfa0bed429"
    "74d465c02c4ab8489369eabc799a374141eb5d71ae00eb4a28598aa442dc0928"
    "8bce662640629106597e886daf9b6c5c12f29fe11f187116d8b49f248825380f"
)
m_tilde = int.from_bytes(bytes.fromhex(m_tilde_hex), "big")

# ------------------------------------------------------------------
# 1. factor N
p = gcd(m_tilde * m_tilde - c, N)
q = N // p
assert p * q == N, "factorisation failed"

print("p =", p)
print("q =", q)

# ------------------------------------------------------------------
# 2. correct Rabin decryption (with the Legendre bits)
def sqrt_mod_3mod4(a, prime):
    """square-root modulo a prime ≡ 3 mod 4"""
    return pow(a, (prime + 1) // 4, prime)

mp = sqrt_mod_3mod4(c, p)
if ((pow(mp, (p - 1) // 2, p) - lp) % p) != 0:
    mp = p - mp                     # flip sign if Legendre bit mismatches

mq = sqrt_mod_3mod4(c, q)
if ((pow(mq, (q - 1) // 2, q) - lq) % q) != 0:
    mq = q - mq

