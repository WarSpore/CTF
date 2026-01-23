from pwn import *

c1 = 'dfc951cfd6a9ed8e6d05ab1c0db08aae25a76890d56901700000000000000000000000000000000000000000000000c0'
c2 = '754709425f0363d6e08c0192553d0304abffe5197fe759fd7c00000000000000000000000000000000000000000000c8'

print(xor(bytes.fromhex(c1),bytes.fromhex(c2)).hex())

t1 = 'ce3141cd2e1288a138ef8e55bdf54ed5'
t2 = 'c6e5f4d454408ab3d328b9eb7c996fbb'

print(xor(bytes.fromhex(t1),bytes.fromhex(t2)).hex())

y_0 = '7b55e15faaaad0367bf885ec20b9e015'
t3 = 'cdce7aca9f6a4c83de57952e00dcb00f'
print(xor(bytes.fromhex(y_0),bytes.fromhex(t3)).hex())