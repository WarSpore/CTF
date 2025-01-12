from Crypto.Util.number import bytes_to_long, getStrongPrime
import math
from Crypto.Util.number import long_to_bytes
from decimal import Decimal, getcontext
from sympy import symbols, Eq, solve

ptxt_bytes = long_to_bytes(38953041933735193343752139097284083802674026778866110094897904307752206884437296361792637)
decoded_string = ptxt_bytes.decode('latin-1')
print(decoded_string)