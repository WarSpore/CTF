from math import *
from Crypto.Util.number import long_to_bytes

def encrypt_chunk(plaintext, iv, key):
    xored = bytes(a ^ b for a, b in zip(plaintext, iv))
    xored_as_int = int.from_bytes(xored, 'big')
    key_as_int = int.from_bytes(key, 'big')
    
    exponent = key_as_int / 2**32 + 0.5
    perturbed_value = sin(key_as_int) * 1337
    
    ct = int(round(xored_as_int ** exponent + perturbed_value))
    
    return ct.to_bytes(6, 'big')

def decrypt_chunk(ct, iv, key):
    key_as_int = int.from_bytes(key, 'big')
    ct_int = int.from_bytes(ct, 'big')
    
    exponent = key_as_int / 2**32 + 0.5
    perturbed_value = sin(key_as_int) * 1337
    
    # Ensure we undo the perturbation safely
    unperturbed_ct = ct_int - round(perturbed_value)
    
    # Reverse the exponentiation safely
    xored_as_int = int(round(unperturbed_ct ** (1 / exponent)))
    
    # Convert back to bytes
    xored_bytes = xored_as_int.to_bytes(4, 'big')
    
    # XOR with IV to get original plaintext
    plaintext = bytes(a ^ b for a, b in zip(xored_bytes, iv))
    
    return plaintext

def encrypt_bytes(plaintext, iv, key):
    ciphertext = bytearray(iv)  # Store IV at the start
    for i in range(0, len(plaintext), 4):
        plain_chunk = plaintext[i:i+4]
        while len(plain_chunk) < 4:
            plain_chunk += b' '  # Pad if needed
        
        encrypted_chunk = encrypt_chunk(plain_chunk, iv, key)
        ciphertext.extend(encrypted_chunk)
        
        # Update IV with last 4 bytes of encrypted chunk
        iv = encrypted_chunk[-4:]
    
    return ciphertext.hex()

def decrypt_bytes(ciphertext_hex, iv, key):
    ciphertext = bytes.fromhex(ciphertext_hex)
    plaintext = bytearray()
    
    iv = ciphertext[:4]  # Extract IV
    ciphertext = ciphertext[4:]  # Remove IV from ciphertext
    
    for i in range(0, len(ciphertext), 6):  # Process 6-byte chunks
        cipher_chunk = ciphertext[i:i+6]
        if len(cipher_chunk) < 6:
            continue  # Skip if not full chunk
        
        decrypted_chunk = decrypt_chunk(cipher_chunk, iv, key)
        plaintext.extend(decrypted_chunk)
        
        # Update IV with last 4 bytes of encrypted chunk
        iv = cipher_chunk[-4:]
    
    return plaintext.strip()

def main():
    iv = 0xdec0de17.to_bytes(4, 'big')
    key = 0xe66faced.to_bytes(4, 'big')
    
    ciphertext = 'dec0de170d4d0f638c17029b2fa6f66b047042d4e1f7033834e1ccc10605de569aef1099391c765f06e568b1ed8804ced8024aa60fd0df478a8311e566838e17000d67d12005000c81e62f0f0eab36e358bc04813fa85e170672d47181af0f3f74ad3c5000020d0805a505b6b33574fc131fef636214'
    
    plaintext = decrypt_bytes(ciphertext, iv, key)
    print(plaintext.decode('utf-8', errors='ignore'))  # Decode safely

if __name__ == "__main__":
    main()
