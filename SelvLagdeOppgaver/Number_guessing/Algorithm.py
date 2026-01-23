import random
from Crypto.Util.number import getRandomRange, getRandomNBitInteger

def one_encoding(bitstring):
    """
    Return the 1-encoding of a binary string.
    Each substring ends at position i where bit i == '1'
    """
    encodings = []
    for i in range(len(bitstring)):
        if bitstring[i] == '1':
            encodings.append(bitstring[:i+1])
    return encodings

def zero_encoding(bitstring):
    """
    Return the 0-encoding of a binary string.
    Each encoding takes prefix up to i-1 and appends '1',
    if bit i == '0'.
    """
    encodings = []
    for i in range(len(bitstring)):
        if bitstring[i] == '0':
            prefix = bitstring[:i]
            encodings.append(prefix + '1')
    return encodings

def generate_encrypted_table(y, g, p, number, n_bits=32):
    table = []
    bitstring = bin(number)[2:].zfill(n_bits)

    for element in bitstring:
        encryptedEntry = []
        
        if element == "0":
            k = getRandomRange(1, p)
            a1 = pow(g,k,p)
            b1 = 1*pow(y,k,p)%p
            
            k = getRandomRange(1, p)
            a2 = pow(g,k,p)
            r = getRandomRange(1,p)
            b2 = r*pow(y,k,p)%p
    
            encryptedEntry.append((a1,b1))
            encryptedEntry.append((a2,b2))

        if element == "1":
            k = getRandomRange(1, p)
            a1 = pow(g,k,p)
            b1 = 1*pow(y,k,p)%p
            
            k = getRandomRange(1, p)
            a2 = pow(g,k,p)
            r = getRandomRange(1,p)
            b2 = r*pow(y,k,p)%p
            
            encryptedEntry.append((a2,b2))
            encryptedEntry.append((a1,b1))
        
        table.append(encryptedEntry)
    
    return table


p = 1552518092300708935130918131258481755631334049434514313202351194902966239949102107258669453876591642442910007680288864229150803718918046342632727613031282983744380820890196288509170691316593175367469551763119843371637221007210577919
g = 2 
x = getRandomRange(1, p)
numberToGuess = getRandomNBitInteger(32)
y = pow(g,x,p)

encrypted_table = generate_encrypted_table(y,g,p,numberToGuess)

# for i, row in enumerate(encrypted_table):
#     print(f"Bit position {i}:")
#     for j, (c1, c2) in enumerate(row):
#         inverse = pow(c1,-x,p)
#         decrypted = (inverse*c2)%p
#         print(f"  Entry {j}: Decrypted value = {decrypted}")


bobGeneratedNumber = getRandomNBitInteger(32)
bobBitstring = bin(bobGeneratedNumber)[2:].zfill(32)
bob0Encoded = zero_encoding(bobBitstring)

cts = []

for bitelement in bob0Encoded:
    ct = [1, 1]
    for index, bit in enumerate(bitelement):
        a, b = encrypted_table[index][int(bit)]
        ct[0] = (ct[0] * a) % p
        ct[1] = (ct[1] * b) % p

    cts.append(tuple(ct))

while len(cts) < len(encrypted_table):
    k = getRandomRange(1, p)
    a = pow(g,k,p)
    r = getRandomRange(1,p)
    b = r*pow(y,k,p)%p
    cts.append((a,b))

import random
random.shuffle(cts)
print(cts)
for a, b in cts:
    shared = pow(a, x, p)
    inv = pow(shared, -1, p)
    decrypted = (b * inv) % p
    if decrypted == 1:
        print("x > y",numberToGuess,bobGeneratedNumber)
        exit(0)
print("x <= y",numberToGuess,bobGeneratedNumber)







