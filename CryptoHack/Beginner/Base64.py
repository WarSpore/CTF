import base64

b64 = '72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf'

b64 = bytes.fromhex(b64)

print(base64.b64encode(b64))
