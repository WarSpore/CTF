import random
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Util.number import long_to_bytes
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from Crypto.Util.number import bytes_to_long
import base64
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os
import datetime
import base64

# Function to derive a key from the given date and time
def derive_key_from_datetime(dt):
    # Convert datetime to a string, then to bytes
    key_str = dt.strftime("%Y%m%d%H%M").encode()  # Example: '202409201422'
    # Ensure the key is 32 bytes long for AES-256
    print(int(key_str)/1000000)
    return key_str.ljust(32, b'\0')[:32]  # Pad with zeros if necessary

def decrypt_aes(ciphertext, key):
    # Decode the base64 encoded ciphertext if needed
    # ciphertext = base64.b64decode(ciphertext)  # Uncomment if ciphertext is base64 encoded
    iv = ciphertext[:16]  # The first 16 bytes are the IV


# Main function to run the decryption
def main():
    # Define the date and time
    for i in range(40):
        dt = datetime.datetime(2024, 9, 20, 14, 22)
        key = derive_key_from_datetime(dt)

        # Example ciphertext (This should be the actual ciphertext you want to decrypt)
        # For the example, this ciphertext is a placeholder. Replace it with your actual ciphertext.
        # If you are using base64 encoded ciphertext, uncomment the base64 decoding line in decrypt_aes.
        # ciphertext = base64.b64decode('...')  # Use actual base64 encoded ciphertext here
        # Example: Assuming the ciphertext is a byte string
        ciphertext = "U2FsdGVkX1+/39qrCQ9rlxMW2E30ylTUXYS+GTAVDMUK0oXJvkUDBCRbhClK2GKYc50OQZ7zgLPBhkMW8CM5VVnZBrxfyH5CAG8nj5BPDCg="
        ciphertext = base64.b64decode(ciphertext)
        # Decrypt the message
        decrypted_message = decrypt_aes(ciphertext, key)
        print("Decrypted message:", decrypted_message.decode(errors='ignore'))  # Decode to string

if __name__ == "__main__":
    main()
