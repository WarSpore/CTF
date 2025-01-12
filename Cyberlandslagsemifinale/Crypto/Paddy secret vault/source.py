from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

secret = open("C:\\Users\\User\\Vscode\\Ctf\\Cyberlandslagsemifinale\\Crypto\\Paddy secret vault\\flag.txt", "rb").read().decode()
admin_key = open("Cyberlandslagsemifinale\\Crypto\\Paddy secret vault\\admin_key.bin", "rb").read()
admin_message = b"I am the administrator of this system and know the admin_key, show me the secret!"

def decrypt(ct):        
    iv = ct[0:16]
    ct = ct[16:]
    cipher = AES.new(admin_key, AES.MODE_CBC, iv)
    return unpad(cipher.decrypt(ct), 16)

def Challenge():
    print(f"Welcome to Paddy's Secret Vault. It's still in a beta version, hopefully without any vulnerabilities.")
    print(f"If you send the AES CBC encrypted 'admin_message' you will learn the secret!")
        
    while True:
        try:
            ct = bytes.fromhex(input("encrypted admin_message (hex)> "))
            pt = decrypt(ct)
            if pt == admin_message:
                print("You are the admin and the secret is", secret)                
                quit()

            print("you are not the admin, try harder.")
        except:
            print("error")

if __name__ == "__main__":
    try:
        Challenge()
    except Exception:
        print("error")
        exit(0)

"""
A good methodology when solving remote crypto CTFs is to solve the challenge locally
first before you try to run your solver against the remote.

In this challenge you lack two files; 'flag.txt' and 'admin_key.bin'. You can create
them with some random content. Obviously, the remote has other content.

    admin_key = os.urandom(16)
    with open("admin_key.bin", "wb") as fd:
        fd.write(admin_key)

    with open("flag.txt", "wb") as fd:
        fd.write("flag{not_the_real_flag}")

Now you can interact with this file locally by running this script, to start building your attack:

    from pwn import process
    io = process(["python","./source.py"])
    io.interactive()

Once your attack succeeds locally you try against the servers endpoint by switcing to pwntools `remote`:

    from pwn import remote
    io = remote("<host>",<port>)
    io.interactive()


To send bytes in hex format you can use the `.hex()` function, like this:

    io.sendline( ("A"*16).encode().hex() )

"""