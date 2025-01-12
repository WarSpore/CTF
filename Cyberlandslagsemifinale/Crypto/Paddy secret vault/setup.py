import os

admin_key = os.urandom(16)
with open("Cyberlandslagsemifinale\Crypto\Paddy secret vault\\admin_key.bin", "wb") as fd:
    fd.write(admin_key)

with open("Cyberlandslagsemifinale\Crypto\Paddy secret vault\\flag.txt", "wb") as fd:
    fd.write(b"flag{not_the_real_flag}")