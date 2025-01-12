# def a(x):
#     return x + 5

# def b(x):
#     return x * 67

# def c(x):
#     return x % 100

# def d(x):
#     return x % 2 == 0

# def e(x):
#     return x // 4

# def f(x, y):
#     return x % y

# def gyldig(tall):
#     tall = int(tall)

#     return c(f(b(a(tall)), e(tall))) == 13 and d(tall)

# for x in range(-10000,10000):
#     try:
#         if(gyldig(x)):
#             print(x)
#     except:
#         a = 1


def gyldig(verdi):
    a = 0
    b = 0
    for c in verdi:
        if c == '9':
            return False

        if c.isupper():
            a += 1
        
        b += ord(c)

        if c == 'a':
            return False
    print(a,b,len(verdi))
    return a == 5 and b == 400 and len(verdi) == 10


print(gyldig("AAAAA#####"))



# def gyldig(verdi):
#     a = verdi
#     b = a[0:5] + a[-5:-3]
#     print(b)
#     c = a[7:-10]
#     print(c)
#     d = a[6] + c[:2] + b
#     print(len(d),len('hei sveis!'))
#     print(d)
#     return d == "hei sveis!"



# print(gyldig(" sveifhei klmnoss!sts")) 

