from pwn import xor

ct = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"

ctb = bytes.fromhex(ct)

for byte in range(256):
    res = xor(ctb,byte)
    if b"crypto" in res:
        print(res)