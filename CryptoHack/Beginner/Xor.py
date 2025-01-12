from pwn import xor

string = b"label"

print(xor(string,13))