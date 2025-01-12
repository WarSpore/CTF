#!/usr/bin/python3 -u
import os.path
from pwn import *

KEY_FILE = "key"
KEY_LEN = 50000
FLAG_FILE = "flag"


def startup(key_location):
	flag = open(FLAG_FILE).read()
	kf = open(KEY_FILE, "rb").read()

	start = key_location
	stop = key_location + len(flag)

	key = kf[start:stop]
	key_location = stop

	result = list(map(lambda p, k: "{:02x}".format(ord(p) ^ k), flag, key))
	print("This is the encrypted flag!\n{}\n".format("".join(result)))

	return key_location

def encrypt(key_location):
	ui = input("What data would you like to encrypt? ").rstrip()
	if len(ui) == 0 or len(ui) > KEY_LEN:
		return -1

	start = key_location
	stop = key_location + len(ui)

	kf = open(KEY_FILE, "rb").read()

	if stop >= KEY_LEN:
		stop = stop % KEY_LEN
		key = kf[start:] + kf[:stop]
	else:
		key = kf[start:stop]
	key_location = stop

	result = list(map(lambda p, k: "{:02x}".format(ord(p) ^ k), ui, key))

	print("Here ya go!\n{}\n".format("".join(result)))

	return key_location


print("******************Welcome to our OTP implementation!******************")
# c = startup(0)
# while c >= 0:
# 	c = encrypt(c)
encflag = "51124f4d194969633e4b52026f4c07513a6f4d05516e1e50536c4954066a1c57"
strflag = "QOMIic>KRoLQ:oMQnPSlITjW"
print(strflag, len(strflag))


p = remote("mercury.picoctf.net", 58913)
p.sendlineafter(b"What data would you like to encrypt?",b"A"*(KEY_LEN-len(strflag)-1))
p.recvuntil(b"Here ya go!\n")

p.sendline(b"a"*(len(encflag)//2))
p.recvuntil(b"Here ya go!\n")
a = p.recvline().decode().strip()
print(a)
p.close()
d = "a"*(len(encflag)//2)

b = "FKO:1=QW=Q8=S==="

li = [3,70,75,79,26,28,58,49,61,25,81,87,61,25,81,2,56,61,25,7,83,61,25,5,3,61,25,4,4,61,25,4]
k = []
for i in range(len(b)):
	k.append(ord(d[i])^(li[i]))
# for i in k:
# 	print(chr(i),end="")
lis = [81,18,79,77,25,73,105,99,62,75,82,2,111,76,7,81,58,111,77,5,81,110,30,80,83,108,73,84,6,106,28,87]
for i in range(len(b)):
	print(chr((lis[i])^(k[i])),end="")










# with open("PicoCTF\Crypto\\tall.txt","w") as file:
# 	a = ""
# 	for i in range(32):
# 		a += "1"
# 	file.write(a)
# b = "mIRmImIPRmIWSmI"
# c = []
# for i in b:
# 	c.append(ord("1")^ord(i))
# print(len(c))
# for i in range(len(strflag)):
# 	print(ord(strflag[i])^c[i],end="")