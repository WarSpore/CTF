from pwn import *
from base64 import b64encode,b64decode
import ast
import json
r = remote("challs.glacierctf.com", 13387)
orig = b"admin=0;name=123"
mod = b"admin=1;name=123"
iv = r.recvuntil(b"1) Get a token")
r.sendline(b"1")
r.recvuntil(b"Hey, what's your name?")
r.sendline(b"123")
r.recvuntil(b"Here is your token: ")
dic = r.recvline().strip().decode()
dic = ast.literal_eval(dic)
iv = dic["iv"]
ct = dic["ct"]
ivmod = xor(xor(orig,mod),b64decode(iv))
print((ivmod))
ivmod = (b64encode(ivmod))
print((b64decode(ivmod)))
r.sendline(b"2")
r.sendline(json.dumps({'iv':ivmod.decode(), 'ct':ct}))
r.interactive()