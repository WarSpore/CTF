from Crypto.Util.Padding import pad
from pwn import *
import string

# Set up logging
context.log_level = 'info'  # You can set this to 'debug' for more detailed output

# Server details
HOST = 'chal.competitivecyber.club'  # Replace with the server's IP or hostname
PORT = 6001           # Replace with the server's port

# Establish a connection
r = remote(HOST, PORT)
flag = b"}"
# Send some data (example)
character = string.printable
while True:
    for char in character:
        r.recvuntil(b'>')
        test = bytes(char.encode("utf-8")) + flag
        print(test)
        testing_character_with_pad = pad(test,16)
        # print(a)
        filler_characters_to_split_flag = b"aaa"+test
        r.sendline(testing_character_with_pad+filler_characters_to_split_flag)
        response = r.recvline()
        response = response.decode()
        response = response.replace(" Response > ", "")
        # print(response)
        # print(response[0:32],response[64:96])
        if response[0:32] == response[64:96]:
            flag = bytes(char.encode("utf-8")) + flag
            print("hei")
            break

# Interact with the server manually (useful for debugging)
# r.interactive()

# Close the connection
r.close()


