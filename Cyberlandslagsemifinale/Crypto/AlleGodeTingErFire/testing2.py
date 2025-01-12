from Crypto.Util.number import bytes_to_long, getPrime, long_to_bytes, isPrime
from sympy import Eq,solve,symbols
import numpy as np
import string
FLAG = b'flag{fake_flags}flag{fake_flags}flag{fake_flags}'
p = 16567432672540057117
p = 18446744073709551557
#p = 6244941658462216819

li = [123822245971683458448449387,143113169179768741280313191,115326947897120319569223525,138268021383953256444357757]

for i in li:
    print(long_to_bytes(int(i)).decode("utf-8"),end="")

li = [ 2**2,3, 37, 17852010398400078143,459858455002695634470509,334178810386220330301984769]

for i in li:
    print(len(bin(i)),i)

step = len(FLAG) // 4

print(len(str(bytes_to_long(b'a'*step))),bytes_to_long(b'}'*step))

flag_parts = [FLAG[i : i + step] for i in range(0, len(FLAG), step)]

flag_parts = [bytes_to_long(part) for part in flag_parts]


# a_1,b_1,c_1,d_1 = flag_parts[0],flag_parts[1],flag_parts[2],flag_parts[3]

# li = [114, 715, 131070, 4294967294]



# a_2 = li[0]
# b_2 = li[1]
# c_2 = li[2]
# d_2 = li[3]

# x1 = a_1*a_2-b_1*b_2-c_1*c_2-d_1*d_2
# x2 = a_1*b_2+b_1*a_2+c_1*d_2-d_1*c_2
# x3 = a_1*c_2-b_1*d_2+c_1*a_2+d_1*b_2
# x4 = a_1*d_2+b_1*c_2-c_1*b_2+d_1*a_2

# print((2**63-471))

# x1 = -584210810594046517355452820113415197
# x2 = 487268406469160255588161824266067879
# x3 = -604670429592815531484994554730642919
# x4 = 523176388428119814691754655613320989

# print(len(str(584210810594046517355452820113415197)))

# print((getPrime(64)))

# print(len(str(4294967294)))


# eq1 = Eq(a_1*a_2-b_1*b_2-c_1*c_2-d_1*d_2, x1)
# eq2 = Eq(a_1*b_2+b_1*a_2+c_1*d_2-d_1*c_2, x2)
# eq3 = Eq(a_1*c_2-b_1*d_2+c_1*a_2+d_1*b_2, x3)
# eq4 = Eq(a_1*d_2+b_1*c_2-c_1*b_2+d_1*a_2, x4)

# # Solve the system of equations
# # solution = solve((eq1, eq2, eq3, eq4), (a_1,b_1,c_1,d_1,a_2, b_2, c_2, d_2))
# # print(solution)
# # for i in solution.items():
# #     print(int(i[1]))

# 5166804639282591238
# 151708338147718170943520125

# a_2,b_2,c_2,p = symbols('a2 b2 c2 p')

# x1 = -584210810594046517355452820113415197
# x2 = 487268406469160255588161824266067879
# x3 = -604670429592815531484994554730642919
# x4 = 523176388428119814691754655613320989

# lowerBound = bytes_to_long(b'flag{      ')
# upperBound = bytes_to_long(b'flag{}}}}}}')

# print(lowerBound,upperBound)


# # Define the equations
# eq1 = Eq((x1*a_2+x2*b_2+x3*c_2+x4*(p-a_2**2-b_2**2-c_2**2)**(1/2))/p, lowerBound)
# eq2 = Eq((-x1*a_2+x2*b_2-x3*(p-a_2**2-b_2**2-c_2**2)**(1/2)+x4*c_2)/p, lowerBound)
# eq3 = Eq((-x1*c_2+x2*(p-a_2**2-b_2**2-c_2**2)**(1/2)+x3*a_2-x4*b_2)/p, lowerBound)
# eq4 = Eq((-x1*(p-a_2**2-b_2**2-c_2**2)**(1/2)-x2*c_2+x3*b_2+x4*a_2)/p, lowerBound)


# # Solve the system of equations
# solution = solve((eq1,eq2,eq3,eq4), (a_2,b_2,c_2,p)) 

# print(solution)

# p_upper = 17852397961982267392

# p_lower = 17842740888313757696



# a_2 =1 
# b_2 = 100
# c_2 =79791
# d_2 = 4231508203

# p = (x1*a_2+x2*b_2+x3*c_2+x4*d_2)/lowerBound

# print(len(str(int(p))))

# print(int(p))



# a_2 = 0
# b_2 = 0
# c_2 = 0
# d_2 = 0

# p = a_2**2+b_2**2 +c_2**2 + d_2**2



#print(x1,x2,x3,x4)