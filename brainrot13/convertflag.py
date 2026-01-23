from Crypto.Util.number import bytes_to_long, long_to_bytes

pad   = b"OAEP" * 23
L     = bytes_to_long(pad)
print(L)
print(long_to_bytes(8983330448975044831228371650114449863380030502432970224115902539133))