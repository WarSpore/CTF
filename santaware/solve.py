from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad, pad
import os
PNG_SIG = b"\x89PNG\r\n\x1a\n"
files = os.listdir(os.curdir+'\santaware\\')
targets = sorted([f for f in files if f.endswith('.enc')])
key = b""
for file in targets:
    with open(rf"santaware\{file}",'rb') as fil:
        key += fil.read(1)


with open(r"santaware\little-hax0r.png.enc","rb") as fil:
    fil.read(1)
    a = fil.read(16)
    for b in range(1,256):
        for b2 in range(1,256):
            keytry = key+b.to_bytes(1,byteorder='big')+b2.to_bytes(1,byteorder='big')
            cipher = AES.new(keytry, AES.MODE_ECB)
            dectry = cipher.decrypt(a).decode(errors="ignore")
            if "PNG" in dectry:
                key = keytry
                enc = fil.read().strip()
                dec2 = cipher.decrypt(a+enc)
                with open(r"santaware\little-hax0r.png","wb") as fil2:
                    fil2.write(dec2)
                    exit(0)