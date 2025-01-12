ct = "c92b7734070205bdf6c0087a751466ec13ae15e6f1bcdd3f3a535ec0f4bbae66"


from Crypto.Cipher import AES
import hashlib
import random


# /usr/share/dict/words from
# https://gist.githubusercontent.com/wchargin/8927565/raw/d9783627c731268fb2935a731a618aa8e95cf465/words
with open("CryptoHack\AES\Passwords_as_keys\words","r") as f:
    words = [w.strip() for w in f.readlines()]
for word in words:
    keyword = word

    KEY = hashlib.md5(keyword.encode()).digest()

    ciphertext = bytes.fromhex(ct)


    cipher = AES.new(KEY, AES.MODE_ECB)
    decrypted = cipher.decrypt(ciphertext)
    if b"crypto{" in decrypted:
        print(decrypted)
