from pwn import *
from Crypto.Util.number import bytes_to_long, long_to_bytes
from base64 import b64decode, b64encode
import string

cflag1 = 'uASMxtucPf+mwuVCOozr1Q2ohJ6fzGoqg9Fu9BjH'
cflag2 = 'fSzly66FrgtEFPyTwJF5wXu6cpgruIvt5NUWXQKz'
cflag3 = 'qge4daTqwLYUUJSBlBKbLGpYmeND6N11OzNiyFCh'

keylist1 = [b'\xcf', b'e', b'\xef', b'\xad',b'\xa0',b'\xc9', b'\xc4', b'\xc0', b'\xdc', b'\xd6', b'\xe7', b'\xfd', b'\xfb', b'\xf6', b'\x8c', b'\x97', b'\x94', b'\xb4', b'^', b'\\', b'Z', b'o', b'b', b'\x1d', b'\x1a', b'=',b'\xba']
keylist2 = [b'\n', b'&', b'=', b'K', b'M', b'B', b'F', b'm', b't', b'u', b'\x8f', b'\x86', b'\x98', b'\x95', b'\xab', b'\xa0', b'\xbb', b'\xb4', b'\xce', b'\xcf', b'\xcc', b'\xc1', b'\xdd', b'\xd5', b'\xef', b'\xe3', b'\xf1']
keylist3 = [b'\xdd', b'\xdc', b'\xdf', b'\xde', b'\xdb', b'\xd0', b'\xc4', b'\xc1', b'\xf8', b'\xed', b'\xeb', b'\x9f', b'\x80', b'\xa7', b'Z', b'R', b'E', b'B', b'u', b'd', b'f', b'\x1c', b'\x1e', b'\x14', b'\r', b'\x05', b'\x06', b'%']


decoded_flag1 = b64decode(cflag1)
decoded_flag2 = b64decode(cflag2)
decoded_flag3 = b64decode(cflag3)
# print(decoded_flag)
finalli = []
finalli2 = []
finalli3 = []
for byte in decoded_flag1:
    li = []
    for key_byte in keylist1:
        result = xor(byte,key_byte)
        try:
            if result.decode() in (string.printable):
                li.append(result.decode())
        except:
            continue
    finalli.append(li)

for byte in decoded_flag2:
    li = []
    for key_byte in keylist2:
        result = xor(byte,key_byte)
        try:
            if result.decode() in (string.printable):
                li.append(result.decode())
        except:
            continue
    finalli2.append(li)


for byte in decoded_flag3:
    li = []
    for key_byte in keylist3:
        result = xor(byte,key_byte)
        try:
            if result.decode() in (string.printable):
                li.append(result.decode())
        except:
            continue
    finalli3.append(li)


for i in range(len(finalli)):
    a = set(finalli[i])
    b = set(finalli2[i])
    c = set(finalli3[i])
    intersection = a.intersection(b).intersection(c)

# Print the result
    #print(intersection, end= " ")
    print(str(intersection)[2],end="")
        
