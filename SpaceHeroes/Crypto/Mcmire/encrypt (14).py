from Crypto.Cipher import AES
import binascii, os

key = b"3153153153153153"
iv =  os.urandom(16)


cipher = AES.new(key, AES.MODE_CBC, iv)

# encrypted_flag = open('message.enc', 'wb')
# encrypted_flag.write(binascii.hexlify(cipher.encrypt(plaintext)))
# encrypted_flag.close()

encrypted_flag = open('SpaceHeroes\Crypto\Mcmire\message.enc', 'rb')
encrypt_text = encrypted_flag.read()
print(cipher.decrypt(binascii.unhexlify(encrypt_text)))

encrypted_flag.close()

print("hint:", "Dirctor something")

