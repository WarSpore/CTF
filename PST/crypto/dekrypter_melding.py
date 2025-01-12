from Crypto.Cipher import AES
from base64 import b64decode
import json

hemmelighet1 = 0x980daad49738f76b80c8fafb0673ff1b
hemmelighet2 = 0xa3c5a5a81ebc62c6144a9dc1ae5cce11
hemmelighet3 = 0xfc78e6fee2138b798e1e51ed15e0a109
key = hemmelighet1^hemmelighet2^hemmelighet3
print(hex(265434951542696755497319068136291405827))
key = bytes.fromhex("c7b0e9826b971ed41a9c36d7bdcf9003")
# Ensure the key is 32 bytes (AES-256)

with open("PST/crypto/melding.enc", "rb") as f:
    try:
        #data = json.loads(f.read().decode('utf-8'))
        nonce = b64decode("iGfRlHEx5cYvehl2YYZv9w==")
        ciphertext = b64decode("E3nvYDlJHG7R0XBQevJEBAHmoaqOdaI1sfX64d5bF+82cvzdZXhS9IVYVmXgE72kvdkZ+h92mGZ0YLx9pX+PbPPtB/JS")
        tag = b64decode("nAjcHbhnjYtwMAHSHrcHsA==")
        cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
        plaintext = cipher.decrypt_and_verify(ciphertext, tag)
        print("Dekryptert melding: " + plaintext.decode('utf-8'))
    except (KeyError):
        print("Oisann, noe gikk galt!")
