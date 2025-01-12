otp = [23, 2, 0, 5, 13, 16, 22, 7, 9, 4, 19, 21, 18, 10, 20, 11, 12, 14, 6, 1, 3, 8, 17, 15]

with open("PST\Rev\pinneved.txt", "r") as file:
    pinneved = file.read()
li = []
for i in pinneved:
    li.append(chr(ord(i)-2))
n = (len(li)//24)
print(n)
fragmenter = []
for i in range(0, len(li), n):
    fragment = li[i:i+n]
    fragmenter.append(fragment)
print(len(fragmenter))
newli = [0]*24
otp.reverse()
for i,tall in enumerate(otp):
    newli[tall] = fragmenter[i]
with open("PST\Rev\slede.txt", "w") as file:
    for i in newli:
        file.write("".join(i))