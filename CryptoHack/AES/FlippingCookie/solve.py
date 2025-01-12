from pwn import *

c = "e922e1f5861b9ba4301a3f1e968ea99750e41d6ae505cbf1c36acc0bca9a0b8e2a29e1ba3e9540ecb7e165c2188349d5"
given_string = "admin=False;expiry={expires_at}" 
target_string = "admin=True;expiry={expires_at}" 
print(len(target_string),len(b"admin=False;expi"),len(b"admin=True;expir"))

print(xor(b"admin=False;expi",b"admin=True;expir",bytes.fromhex("e922e1f5861b9ba4301a3f1e968ea997")).hex())

def split_into_blocks(ciphertext_hex, block_size=16):
    # Convert the hex string to bytes
    ciphertext_bytes = bytes.fromhex(ciphertext_hex)
    
    # Split the byte array into blocks of the specified size
    blocks = [ciphertext_bytes[i:i + block_size] for i in range(0, len(ciphertext_bytes), block_size)]
    
    # Convert each block back to hex for easy viewing
    block_hex_strings = [block.hex() for block in blocks]
    
    return block_hex_strings

# Example usage
blocks = split_into_blocks(c)

for idx, block in enumerate(blocks):
    print(f"Block {idx + 1}: {block}")
