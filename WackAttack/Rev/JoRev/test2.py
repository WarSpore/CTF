import numpy as np
print(int(hex(105)[2:]))
def custom_function(x):
    return ((81 * x) % 1024) >> 2

def binary_sum(k):
    return k + binary_sum(k - 1) if k > 0 else 0

target = binary_sum(19) + binary_sum(3) + binary_sum(2) - binary_sum(1)
target = 72
for i in range(0,1000):
    if custom_function(i) == 69:
        print(i)

a = (np.array([int(a) for a in "20971503181584631574623195110399999831685157".split("3")]))

# for i in a:
    # print((pow(i,(1/3))+2),end=" ")