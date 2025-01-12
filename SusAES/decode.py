from Crypto.Cipher import AES
from Crypto.Util.number import bytes_to_long, getPrime,long_to_bytes
from Crypto.Util.Padding import unpad
from pwn import xor
flagenc = '1a6325ec0765efaa0d87625f7c5535fe1c4ebb138295a1147e68b4c8625550b5ce295e42692e799158a45e210f4cdf02'
flagdec = 'cfd5601da199eb671eb1cd36af4cce462e53438f6251dbc96cb3046d496406c72b788d25ff9eaa1f7563bfc3695e5bbe'
iv = '9ce72766c2ae8f522d80af01967faa70'

hex_string = "1a6325ec0765efaa0d87625f7c5535fe1c4ebb138295a1147e68b4c8625550b5ce295e42692e799158a45e210f4cdf02"

# Split the string into 4 blocks (32 hex characters per block)
block1enc = hex_string[0:32]
block2enc = hex_string[32:64]
block3enc = hex_string[64:96]
block4enc = hex_string[96:128]


block1dec = flagdec[0:32]
block2dec = flagdec[32:64]
block3dec = flagdec[64:96]
block4dec = flagdec[96:128]

a = xor(bytes.fromhex(iv),bytes.fromhex(block1dec))
b = xor(bytes.fromhex(block1enc),bytes.fromhex(block2dec))
c = xor(bytes.fromhex(block2enc),bytes.fromhex(block3dec))
print((a+b+c))
