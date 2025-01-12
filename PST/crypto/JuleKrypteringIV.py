from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from base64 import b64decode, b64encode

def decrypt_aes_ctr(key, nonce, ciphertext):
    key = b64decode(key)
    nonce = b64decode(nonce)
    ciphertext = b64decode(ciphertext)

    backend = default_backend()
    cipher = Cipher(algorithms.AES(key), modes.CTR(nonce), backend=backend)
    decryptor = cipher.decryptor()
    plaintext = decryptor.update(ciphertext) + decryptor.finalize()

    return plaintext

def encrypt_rot13(text):
    result = ""
    for char in text:
        if char.isalpha():
            offset = 13 if char.islower() else -13
            result += chr(((ord(char) - ord('a' if char.islower() else 'A') + offset) % 26) + ord('a' if char.islower() else 'A'))
        else:
            result += char
    return result

# Example usage
key_hex = "dda2846b010a6185b5e76aca4144069f88dc7a6ba49bf128"
key_base64 = b64encode(bytes.fromhex(key_hex)).decode('utf-8')
nonce = print(encrypt_rot13("UtgangsVektor123"))
ciphertext = "wqpUacKqYz7DiENVw70DBldT4oCexZMR4oSif1Uew43Di8Klf8Krw40Nw5xITMaSf8KNwrQ4wqjihKLDtEV5wqTCrcOMYRDCseKAmcK0w5vCp8W9w47igKLigJTDrMK9w6FyDcOyfiTDvURJw4vDusOIPTbDksOHw41NwqLDpsOCFMOzwrE6H8OwwqDDgSXigLnigLkpXmvCtiHDvh7DoGzCtlbDhX3LhsKd4oCd4oKsw7hbw5JzKS5bJ2IMw4DCtWfFviLCpx5bBsOBVMOjRjIVflhAwqzDmEfLnMOAwqxDxbgsc8Opw4J1OEY1TsOPwrrDgg3Dgy7Dug/CtjvLnHQIYcO8FMO7TMK7wrfCq8OSw7pkLHA3ZlvDuMWgannDtDPDp8Kd4oKswo02IAx8w5Iwwr3Co0p6OD1uCxgURA3LhsOC4oCdw64lJsOWNsOAw4x/w5QcTcKsPz1eaOKEohbCrGHDk8O9d8KPDjVfRsKrxZJwwqbDpxLigJ7DksO4KEtXw4/DnsOow73DjsOlw6bDoMKpFQjDpSvCpjALw5BmduKAoF3DsHzigJzDjsKyw7Y8d2MQw4w="

decrypted_text = decrypt_aes_ctr(key_base64, nonce, ciphertext)
print("Decrypted Text:", decrypted_text)
