from Crypto.Util.Padding import pad, unpad
from Crypto.Util.number import *
from pwn import xor, remote, process

admin_message = b"print(flag)"

#io = process(["python3", "../chall/source.py"])
io = remote("chal.competitivecyber.club",6002, level="ERROR")
io.recvuntil(b"Guest: ")    

def oracle(msg : bytes):
    global io        
    io.sendline(msg.hex().encode())        
    resp = io.readline()
    print(resp)
    if b"Error!\n" in resp:
        return False
    return True

# CBC-R: encryption oracle attack - encrypt a message of our choice
def attack_block(trail):
    suffix = []
    while len(suffix) != 16:        
        for i in range(0xff):
            t = long_to_bytes(i, 1)
            ct = b"\x00"*(15 - len(suffix)) + t + bytes(suffix) + trail            
            if oracle(ct):                
                t = i ^ (len(suffix)+1) ^ (len(suffix)+2)

                # recalculate suffix for next round
                for i,s in enumerate(suffix):
                    n = s ^ (len(suffix)+1) ^ (len(suffix)+2)
                    suffix[i] = n        
                suffix = [t] + suffix
                break

    print(" done")
    return ct

message = pad(b"\x00"*16 + admin_message, 16)
message_blocks = [message[i:i+16] for i in range(0, len(message), 16)]
ciphertext = b"\x00"*16 # start trailing block

for block_i in range(len(message_blocks)-1, -1, -1):
    print(f"[+] attack block_{block_i}", end="")
    ct = attack_block(ciphertext[0:16])
    pt_null = xor(ct[0:16], b"\x10"*16)
    newctblock = xor(pt_null, message_blocks[block_i])
    ciphertext = newctblock + ciphertext

io.sendline(ciphertext[16:].hex().encode())
io.interactive()
flag = io.recvline()
print(flag[flag.find(b"flag{"):])