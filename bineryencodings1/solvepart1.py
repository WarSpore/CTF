from Crypto.Util.number import getPrime, long_to_bytes
import os
def binarify(m):
    return int.from_bytes(bin(int.from_bytes(m, "big")).encode(), "big")

with open ("bineryencodings1\output.txt","r") as fil:
    perLi = fil.readlines()
flag = []
hei = "heipådeg"
pLi = []
fLi = []
for per in range(0,len(perLi),2):
    p = perLi[per][len("p_0 = "):].strip()
    f = perLi[per+1][len("p_0 = "):].strip()
    pLi.append(int(p))
    fLi.append(int(f))
print(pLi)
print(fLi)



