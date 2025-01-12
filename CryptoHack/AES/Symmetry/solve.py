from pwn import xor

ct = "663cea88f54bae000db937a5eec69a2207f859b4ced0f4efa390e27e73e15b975814980186cf62797d4b441698c7892b78"

def split_into_blocks(ciphertext_hex, block_size=16):
    # Convert the hex string to bytes
    ciphertext_bytes = bytes.fromhex(ciphertext_hex)
    
    # Split the byte array into blocks of the specified size
    blocks = [ciphertext_bytes[i:i + block_size] for i in range(0, len(ciphertext_bytes), block_size)]
    
    # Convert each block back to hex for easy viewing
    # block_hex_strings = [block.hex() for block in blocks]
    
    return blocks

# Example usage
blocks = split_into_blocks(ct)
streamc = "648a20c4babf8fdfc5f2bd4f46be6eee3579ab36f4fe014d11146537b9f6b80a0586b0851600ee9b81b6dbf6cfb7bd77"
stremcb = split_into_blocks(streamc)

for i in range(len(stremcb)):
    print(xor(stremcb[i],blocks[i+1]),end="")
print(blocks)
print("0"*32)
