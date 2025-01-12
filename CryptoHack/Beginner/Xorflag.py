from pwn import xor

ct = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"

ctb = bytes.fromhex(ct)

knownp = b"crypto{"
firstpartkey = xor(b"crypto{",ctb[0:len(knownp)])
lastpartkey = xor(b"}",ctb[-1])
print(xor(firstpartkey+lastpartkey,ctb))