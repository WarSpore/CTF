from Crypto.Cipher import AES
from Crypto.Util.number import long_to_bytes, bytes_to_long
from Crypto.Util.Padding import pad
from pwn import *

# Connect to the remote server using netcat via Pwntools
r = remote('ctf.wackattack.eu', 5016)

counter2 = '00000002'
counter3 = '00000003'
counter4 = '00000004'
flaghex = b'666c6167'  # Hex for "flag"
choices = ["CTR", "CBC", "CFB"]
i = 0

# Initial payload to send
payload1 = '00000000000000000000000000000000' * 5
outputs = []
choice = ""
for b in range(3):

    # Receive prompt from the server, expecting the mode selection message
    r.recvuntil(b"What mode do you want to use")
    
    choice = choices[i]
    
    # Print what the server sends before sending the choice
    print(r.recvline().decode().strip())

    # Send the mode choice (CTR, CBC, or CFB) to the server
    r.sendline(bytes(choice,encoding="utf-8"))

    # Print what the server sends after sending the mode choice
    print(choice)
    if choice == "CTR":
        r.recvuntil(b"Give us your input as hex")
        r.sendline(flaghex)
        print(r.recvline().decode().strip())  # Print the response after sending input
        nonce = r.recvline().strip().decode().split("Your nonce: ")[1]
        output = r.recvline().strip().decode().split("Your function output: ")[1]
        outputs.append(output)
        print(f"Nonce: {nonce}")
        print(f"Output: {output}")
        i += 1
        continue

    elif choice == "CBC":
        # For CBC mode, set the text to payload1
        r.recvuntil(b"Give us your input as hex")
        r.sendline(payload1)
        r.recvline()
        output = r.recvline().strip().decode().split("Your function output: ")[1]
        outputs.append(output)
        print(outputs)
        print(f"Output: {output}")
        i += 1
        continue

    elif choice == "CFB":
        r.recvuntil(b"Give us your input as hex")
        plaintext = hex(bytes_to_long(xor(bytes.fromhex(nonce + counter4), bytes.fromhex(outputs[1][96:128]))))
        payload2 = '00000000000000000000000000000000' + '00000000000000000000000000000000' +'00000000000000000000000000000000' + plaintext[2:] + '00000000000000000000000000000000'
        r.sendline(bytes(payload2,encoding="utf-8"))
        r.interactive()
        print(output)
        outputs.append(output)
        print(f"Output: {output}")
        print(outputs)
        print(r.recvline().decode().strip())  # Print the response after sending input
        i += 1
        continue

# Final XOR operation on specific blocks of outputs
outputfinal = '19a9ab7adc10d9538885835606b4e7b41e19ab2b42bf5b31d033cd31ff7ee481356ec7764d5f5a3acd41cf5aa0110e93540de5a4adcdc1a22e44443b00000004791d206b91e5eb37b40d0ec87a453cb37871dfc95f2e621e22e9bed8197d1254'
outputfinal1 = 'f6d12a8274d7406c2f43d657a3c8b12d61aa0ca3d0647363e06b1bef7dd8a4c430103e0400e979c0f4e8172109217722f6dbe090f838cd2ac6c3d7d2ebe9cbc34a73101ef68d963ebd0407c1734c35ba'
result = xor(bytes.fromhex(outputs[0][128:160]), bytes.fromhex(outputfinal[128:160]))

# Print the final XOR result
log.info(f"Result: {result}")

# Close the connection
r.close()
