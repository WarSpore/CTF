import base64

def base_to_hex(data):
    return base64.b64decode(data+"==").hex()

plaintext1 = b"{'saldo': 90, 'varer': ['Banan']}"
ciphertext1_b64, tag1_b64 = "BmKtIdhBoEBaFnYVEwou8RaQhFL8rZIZax/w+t0VBNLr.xUnFMnilk9J9z+1goZYcdA".split('.')

plaintext2 = b"{'saldo': 80, 'varer': ['Mango']}"
ciphertext2_b64, tag2_b64 = "BmKtIdhBoEBaFncVEwou8RaQhFL8rZIZaxDw+tsUBNLr.hK4GROnNzWz38mQMV9WaYA".split('.')

plaintext3 = b"{'saldo': 85, 'varer': ['Ananas']}"
ciphertext3_b64, tag3_b64 = "BmKtIdhBoEBaFncQEwou8RaQhFL8rZIZaxz/9dIaVa3LMA.z2zuOKWn8r0nWa4QDxg5Xw".split('.')

hex_cipher1 = base_to_hex(ciphertext1_b64)
hex_cipher2 = base_to_hex(ciphertext2_b64)
hex_cipher3 = base_to_hex(ciphertext3_b64)
print(base_to_hex(tag3_b64),base_to_hex(tag2_b64))

print("h1:",hex_cipher1)
print("h2:",hex_cipher2)
print("h3:",hex_cipher3)

for i in range(0,96,32):
    print(hex_cipher1[i:i+32])