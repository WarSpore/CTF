#!/usr/bin/env python3

from Crypto.Cipher import AES
from Crypto.Util.number import long_to_bytes
from Crypto.Util.Padding import pad
import secrets


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
    while len(used) < len(ciphers):
        print("What mode do you want to use")
        choice = input("> ")
        if choice not in ciphers:
            print("That mode is not avilable")
            continue
        if choice in used:
            print("You can't use that one again")
            continue
        used.add(choice)
        mode, nonce = ciphers[choice]
        print("Give us your input as hex")
        text = bytes.fromhex(input("> "))
        if b"flag" in text:
            text = b"Oh you want the flag, here you go " + b"FLAG"
        text = pad(text, AES.block_size)
        output = mode.encrypt(text)
        if nonce != b"":
            print(f"Your nonce: {nonce.hex()}")
        print(f"Your function output: {output.hex()}")



if __name__ == "__main__":
    while True:
        cycle()
