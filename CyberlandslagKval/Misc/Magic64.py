flag = "yljIyRÅAÆåÅgUrDgUrfZÆWÅPUWFICåøåzOpgyåfØBtjAyRP"


with open ("CyberlandslagKval\Misc\magi64.txt","r",encoding='utf-8') as fil:
    dicMagic64 = {}
    for i,line in enumerate(fil.readlines()):
        if i < 10:
            dicMagic64[line[5]] = line[0]
        else:
            dicMagic64[line[5]] = line[0:2]
print(dicMagic64)
lis = []
for i in flag:
    lis.append(bin(int(dicMagic64[i]))[2:].zfill(6))
print(" ".join(lis))