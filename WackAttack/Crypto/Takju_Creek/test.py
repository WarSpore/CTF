from Crypto.Util.number import bytes_to_long, long_to_bytes
import random
import os
from mt19937predictor import MT19937Predictor


def encrypt(data):
    data = bytes_to_long(data)
    print(data)
    output = 0
    while data != 0:
        output = output << 32
        print(data)
        print(data & 2**32-1)
        output += (data & 2**32-1) ^ random.getrandbits(32)
        data = data >> 32
    a = (output)
    print(a.bit_length())
    return long_to_bytes(output)

if __name__ == "__main__":
    random.seed(os.urandom(32))
    while True:
        print("Send 1 to encrypt your data")
        print("Send 2 to get the encrypted flag")
        if (choice:=input("> ")) == "1":
            print(encrypt(b'A'*4))
        elif choice == "2":
            print(encrypt("FLAG"))
        else:
            print("Invalid choice")