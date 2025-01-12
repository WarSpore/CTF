from Crypto.Util.number import bytes_to_long, getPrime, long_to_bytes, isPrime
from sympy import Eq,solve,symbols,nextprime
import numpy as np
import string
FLAG = b'flag{fake_flags}flag{fake_flags}flag{fake_fl'
p = 16567432672540057117
p = 18446744073709551557
#p = 6244941658462216819
step = len(FLAG) // 4

# print(len(str(bytes_to_long(b'}'*step))),bytes_to_long(b'}'*step))
FLAG = b' '*len(FLAG)
FLAG = b'}'*len(FLAG)
flag_parts = [FLAG[i : i + step] for i in range(0, len(FLAG), step)]

flag_parts = [bytes_to_long(part) for part in flag_parts]


a_1,b_1,c_1,d_1 = flag_parts[0],flag_parts[1],flag_parts[2],flag_parts[3]


li = [114, 715, 131070, 4294967294]

a_2 = li[0]
b_2 = li[1]
c_2 = li[2]
d_2 = li[3]

x1 = a_1*a_2-b_1*b_2-c_1*c_2-d_1*d_2
x2 = a_1*b_2+b_1*a_2+c_1*d_2-d_1*c_2
x3 = a_1*c_2-b_1*d_2+c_1*a_2+d_1*b_2
x4 = a_1*d_2+b_1*c_2-c_1*b_2+d_1*a_2

li = [100000,2000000,2000000,2000000]

li = [114, 715, 131070, 4294967294]

#li = [314,2631,109524,3037000498]

x1 = -584210810594046517355452820113415197
x2 = 487268406469160255588161824266067879
x3 = -604670429592815531484994554730642919
x4 = 523176388428119814691754655613320989

a_2 = li[0]
b_2 = li[1]
c_2 = li[2]
d_2 = li[3]

#print(x1,x2,x3,x4)

a_1,b_1,c_1,d_1 = symbols('a1 b1 c1 d1')
eq1 = Eq(a_1*a_2-b_1*b_2-c_1*c_2-d_1*d_2, x1)
eq2 = Eq(a_1*b_2+b_1*a_2+c_1*d_2-d_1*c_2, x2)
eq3 = Eq(a_1*c_2-b_1*d_2+c_1*a_2+d_1*b_2, x3)
eq4 = Eq(a_1*d_2+b_1*c_2-c_1*b_2+d_1*a_2, x4)

solution = solve((eq1, eq2, eq3, eq4), (a_1, b_1, c_1, d_1))
#print(solution)
for i in solution.items():
    print(int(i[1]))
print(flag_parts[0])
    