phi_N = (p^3-1)*(p^3-p)*(p^3-p^2)* (q^3-1)*(q^3-p)*(q^3-p^2)

# General formula for phi which is not phi but using group linear algebra s is the order of the matrix (n*n), this number is every way to invert the matrix in the field F_N 
# https://www.youtube.com/watch?v=DEQTIr0mBS8&ab_channel=Dr.MajidKhanMathematicsWaley

for k in range(s):
    ps *= (p**s-p**k)
    qs *= (q**s-q**s)
phi = ps*qs