import string

LOWERCASE_OFFSET = ord("a")
ALPHABET = string.ascii_lowercase[:16]
def b16_encode(plain):
	enc = ""
	for c in plain:
		binary = "{0:08b}".format(ord(c))
		enc += ALPHABET[int(binary[:4], 2)]
		enc += ALPHABET[int(binary[4:], 2)]
	return enc

def shift(c, k):
	t1 = ord(c) - LOWERCASE_OFFSET
	t2 = ord(k) - LOWERCASE_OFFSET
	return ALPHABET[(t1 + t2) % len(ALPHABET)]

C = "lkmjkemjmkiekeijiiigljlhilihliikiliginliljimiklligljiflhiniiiniiihlhilimlhijil"

for o in ALPHABET:
	key = o
	svar = ""
	dic = {}
	for y in range(0,len(C),2):
		
		for x in string.printable:
			flag = x
			assert all([k in ALPHABET for k in key])
			assert len(key) == 1

			b16 = b16_encode(flag)
			enc = ""
			for i, c in enumerate(b16):
				enc += shift(c, key[i % len(key)])
			try:
				if enc == C[y:y+2]:
					dic[flag] = enc
					svar += flag
			except:
				break
	if len(svar) == 39:
		print(dic)
		print(key)
		print(svar,len(svar))






