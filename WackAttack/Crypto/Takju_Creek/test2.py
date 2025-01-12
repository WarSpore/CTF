from Crypto.Util.number import bytes_to_long, long_to_bytes

a = b'Z\xb5\xd0\xea'

print(bytes_to_long(a).bit_length())