from Crypto.Cipher import AES
from Crypto.Util.Padding import pad,unpad
from random import choices, randint
from string import printable
import sys, os

c1 = "3c710f988259366f3ceba4e29dd5d2ba40676893c72659399693c8505e20249f9fcdfcdc87755b94e7ab130dfb417d4b21ae7e3428ab6d2d526d884a7e21d7d4dc50a7eb264a39d0187db9a962d44b5dda10ed5bf7b4e314d84da579c5c06fc1080482cfa1e967107b34323aa9b02a0f"
c2 = "3c710f988259366f3ceba4e29dd5d2baf42459d828cd4aa80a4ee1390761f9e27c5abf2188554885708016faee804869"
c3 = "3c710f988259366f3ceba4e29dd5d2ba3499d3b5586ffbc3f0838a3a1bdb20f0a8610aef042dc87e5e0d454ee77898d90103ce3a73dbaf4a75ffbcc35d2feb098feef53861abda2b96bc468f9693d8cf"
c4 = "3c710f988259366f3ceba4e29dd5d2bac11afef885ce0686bd7ef6ddf427ee23080482cfa1e967107b34323aa9b02a0f"
c5 = "3c710f988259366f3ceba4e29dd5d2ba4e5a9d62a3ca13c602eb1a6ecd9b213427875d1de6549c8e44b3d4f31aecddbc7b44ba3555d822706fc1082ab22eeaa1602b54cbddf1beb87a9bef7364d46f86003d110035caf305bf1acf8d5188dd3480e264f25679d0603e2fe0aeb9fe2f5419164739264ac8a73d58d6092722d5a8"
f1 = "522c1c08647dffdcfd6c9f299256d06c73adfc42def86d9551be0a096404b5415ddafc38492c9fced85d86c97655121e3d9623150d9f4a1a2b2a1778d19a019c20ff7bf7341c285f7e73abac9508de6a3666c5205730812dc3c3c44e6904b3e672ae12418ba154a0f286ea6f2aea956ddce2455dff4372d4c7d0934769fb43aceee45a7d9fb5024447e0cef30057e359"

li = [c1,c2,c3,c4,c5]
for c in li:
    for i in range(1,256):
        byte_array = bytearray([i] * 16)
        key = bytes(byte_array)
        ciph = AES.new(key, AES.MODE_ECB, )
        d = ciph.decrypt(bytes.fromhex(c))
        try:
            d  = unpad( d, AES.block_size, )
            if b"a"*16 in d:
                print(d)
        except:
            continue

key = b"\x8a\xc12VP\xa5w\x98\x14\xa3\xdaQ3\xd5Fh"
ciph = AES.new(key, AES.MODE_ECB)
d = ciph.decrypt(bytes.fromhex(f1))
print(d)