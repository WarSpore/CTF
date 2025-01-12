from Crypto.Util.number import bytes_to_long, getStrongPrime
import math
from Crypto.Util.number import long_to_bytes
from decimal import Decimal, getcontext
from sympy import symbols, Eq, solve

ptxt_bytes = long_to_bytes(3332311333311333132)
decoded_string = ptxt_bytes.decode('latin-1')
print(decoded_string)