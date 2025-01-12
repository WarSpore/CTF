import string

dic = {}

for i in string.ascii_lowercase:
    dic[i] = 0


flaggtall = [94,44,44,66,49,67,33,76,56,55,43,53]

with open ('SpringForward\\Crypto\\underworld.txt','r') as fil:
    for i in fil.read():
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1

print(dic)