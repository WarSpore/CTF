import numpy as np

def binary_sum(k):
    return k + binary_sum(k - 1) if k > 0 else 0

def custom_function(x):
    return ((81 * x) % 1024) >> 2

i = "wack{numpy_15_w1ErD}"

l = (np.array([sum(f) for f in list(zip((ord(e) for e in i),[5]*len(i)))]))

seed = ord('w')+5

np.random.seed(seed)

a = {"size":len(l)}
k = np.random.randint(0, 183, **a)
assert l[3:][k[:-3] % 4 == 3][0] == 115

assert (custom_function(l[3:][k[:-3] % 4 == 2]) == np.array([207, 105, binary_sum(19) + binary_sum(3) + binary_sum(2) - binary_sum(1), 72])).all()
print(l)
print(l[3:][k[:-3] % 4 == 1])
print((l[3:][k[:-3] % 4 == 1] ** 3 - 2))
print(np.array([int(a) for a in "20971503181584631574623195110399999831685157".split("3")]))
assert (l[3:][k[:-3] % 4 == 1] ** 3 - 2 == np.array([int(a) for a in "20971503181584631574623195110399999831685157".split("3")])).all()

# assert (l[3:][k[:-3] % 4 == 0] ^ -4 == np.array([-116, -114, -119, -126, -104, -106])).all()

