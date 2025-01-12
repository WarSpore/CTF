from pwn import *
from Crypto.Util.number import bytes_to_long, long_to_bytes
from base64 import b64decode, b64encode


flagc = "evc5tIIsZm7sNa7vq8w0Cv6B9SMo/CoOWRRzOxLN"

decoded_flag = b64decode(flagc)

first_five_bytes = decoded_flag[:5]

first_five_key = xor(b"wack{",first_five_bytes)
print(bytes_to_long(b"w"))
print(len(first_five_key))