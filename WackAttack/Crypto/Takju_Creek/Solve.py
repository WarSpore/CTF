from pwn import *
from mt19937predictor import MT19937Predictor
from Crypto.Util.number import bytes_to_long, long_to_bytes

r = remote('ctf.wackattack.eu', 5027)


r.recvuntil("Send 1 to encrypt your data")
r.sendline(b"1")
data = b'0' * 2496
r.sendlineafter(b"plaintext: ",data)
output = r.recvuntil(b"\n")
r.sendline(b"2")
r.recvuntil(b">")
flag = r.recvline()
predictor = MT19937Predictor()
output = output.decode("utf-8")
flag = flag.decode("utf-8")
r.close()
print(output)
output = output[2:]
output = output[:-1]
output = bytes(output,encoding="utf-8")

flag = flag[3:]
flag = flag[:-1]
flag = bytes(flag,encoding="utf-8")
n = 0
for i in range(0,2496,4):
    x = output[i:i+4]
    predictor.setrandbits(bytes_to_long(x)^808464432, 32)
    n += 1

for i in range(0,len(flag),4):
    decflag = xor(long_to_bytes(predictor.getrandbits(32)),flag[i:i+4])
    print(decflag,end="")