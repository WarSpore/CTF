import secrets

from Crypto.Util.strxor import strxor
from Crypto.Util.number import long_to_bytes, bytes_to_long
from Crypto.Util.Padding import pad


BLOCK_SIZE = 10
NONCE = secrets.token_bytes(10)
KEY = secrets.token_bytes(8)+b"\x00"*2
ALPHABET = b"".join(chr(i).encode() for i in range(127))

def vig(pt: bytes, key: bytes):
    return b"".join(chr((p+k)%128).encode() for p, k in zip(pt,key))

def block_encrypt(pt: bytes, i: int):
    new_nonce = long_to_bytes(bytes_to_long(NONCE)+i)
    print(vig(new_nonce, KEY))
    #strxor pt and key+nonce and nonce last 2 bytes
    return strxor(pt, vig(new_nonce, KEY))

def encrypt(pt: bytes):
    if len(pt) % BLOCK_SIZE != 0:
        raise Exception("Plaintext must be divisable with block length")
    ct = b""
    i = 0
    while i < len(pt) // BLOCK_SIZE:
        ct += block_encrypt(pt[i*BLOCK_SIZE:(i+1)*BLOCK_SIZE], i)
        i += 1
    return ct

if __name__ == "__main__":
    data = b"0"*4590
    pt = pad(data, BLOCK_SIZE)
    ct = encrypt(pt)
