import hashlib
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad,unpad


b = 11131221131211131231121113112221121321132132211331222113112211

r = 311311222113111231131112132112311321322112111312211312111322212311322113212221
temp = str(r)[0]
n = 0
li = []
for i in str(r):
    if temp != i:
        li.append([str(n),temp])
        temp = i
        n = 1
        continue
    n += 1
key = ""
for i in li:
    key += i[0]+i[1]
key += '11'
print(key)
h = hashlib.sha256()
h.update(str(key).encode())
key = h.digest()

cipher = AES.new(key, AES.MODE_ECB)
flag = "f143845f3c4d9ad024ac8f76592352127651ff4d8c35e48ca9337422a0d7f20ec0c2baf530695c150efff20bbc17ca4c"
decrypt = cipher.decrypt(bytes.fromhex(flag))
#print(decrypt)
print(unpad(decrypt,16))

