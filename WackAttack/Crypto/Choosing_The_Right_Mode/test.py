from Crypto.Cipher import AES
from Crypto.Util.number import long_to_bytes,bytes_to_long
from Crypto.Util.Padding import pad
from pwn import *

counter2 = '00000002'

#89034aa0e441ec8d0e95d47c650b1516

#!/usr/bin/env python3

from Crypto.Cipher import AES
from Crypto.Util.number import long_to_bytes
from Crypto.Util.Padding import pad
import secrets

flaghex = '666c6167'

def getCiphers():
    IV = long_to_bytes(secrets.randbits(8*16))
    nonce = long_to_bytes(secrets.randbits(8*12))
    key = long_to_bytes(secrets.randbits(8*32), 32)
    ciphers = {
        "CBC" : (AES.new(key, AES.MODE_CBC, IV), b""),
        "CTR" : (AES.new(key, AES.MODE_CTR, nonce=nonce), nonce),
        "CFB" : (AES.new(key, AES.MODE_CFB, IV, segment_size=128), b""),
    }
    return ciphers

def cycle():
    used = set()
    ciphers = getCiphers()
    choices = ["CTR","CBC","CFB"]
    i = 0
    payload1 = '00000000000000000000000000000000'*3
    outputs = []
    for b in range(3):
        text = flaghex
        print("What mode do you want to use")
        choice = choices[i]
        print(choice)
        if choice =="CBC":
            text = payload1
        if choice == "CFB":
            plaintext = hex(bytes_to_long(xor(bytes.fromhex(noncep+counter2),bytes.fromhex(outputs[1][32:64]))))
            print(plaintext[2:])
            payload2 = '00000000000000000000000000000000'+plaintext[2:]+'00000000000000000000000000000000'
            text = payload2
        used.add(choice)
        mode, nonce = ciphers[choice]
        text = bytes.fromhex(text)
        print("Give us your input as hex")
        if b"flag" in text:
            text = b"Oh you want the flag, here you go " + b"FLAG"
        text = pad(text, AES.block_size)
        output = mode.encrypt(text)
        if nonce != b"":
            noncep = nonce.hex()
            print(f"Your nonce: {nonce.hex()}")
        
        print(f"Your function output: {output.hex()}")
        outputs.append(output.hex())
        i += 1
    print(xor(bytes.fromhex(outputs[0][64:96]),bytes.fromhex(outputs[2][64:96])))



if __name__ == "__main__":
    cycle()
