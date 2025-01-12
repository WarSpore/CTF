from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad


def split_into_blocks(ciphertext_bytes, block_size=16):
    # Convert the hex string to bytes
    # Split the byte array into blocks of the specified size
    blocks = [ciphertext_bytes[i:i + block_size] for i in range(0, len(ciphertext_bytes), block_size)]
    
    # Print the blocks
    for idx, block in enumerate(blocks):
        print(f"Block {idx + 1}: {block.hex()}")  # Convert each block back to hex for easy viewing


KEY = b"3"*16
FLAG = "crypto{sadfasdfasasdfdsadfadffsa}"

def encrypt(plaintext):
    plaintext = bytes.fromhex(plaintext)

    padded = pad(plaintext + FLAG.encode(), 16)
    split_into_blocks(padded)
    cipher = AES.new(KEY, AES.MODE_ECB)
    try:
        encrypted = cipher.encrypt(padded)
    except ValueError as e:
        print("error")

    # print("ct: ", encrypted.hex())
    # print(encrypted.hex())

for b in range(1):
    for i in range(16,32):
        p = hex(i)[2:]
        attempt = pad(bytes.fromhex(p),16).hex()
        plaintext_input = attempt+"ff"*15
        # print("Plaintext_input: ",plaintext_input)
        # print("Attempt: ", attempt)
        encrypt(plaintext_input)