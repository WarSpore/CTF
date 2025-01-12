def extendedgcd(a, b):

    if b == 0:
        return 1, 0
    else:
        x1, y1 = extendedgcd(b, a % b) 
        x = y1
        y = x1 - (a // b) * y1
        return x, y

p=26513
q=32321
x, y = extendedgcd(p, q)
print(f"x: {x}, y: {y}")
