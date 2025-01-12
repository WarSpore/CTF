import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
from pwn import *

# Generate a dataset from a normal distribution with mean 0 and sigma 0.35
mu = 0  # mean
sigma = 0.35  # standard deviation
num_samples = 1000  # number of samples

r = remote("10.212.138.23",22835)

# Function to perform normality tests
for i in range(299):
    r.recvuntil(b"Uniform [0] or a public key [1]?")
    numbers = r.recvuntil(b'>').strip().decode()
    numbersList = numbers.split(",")
    data = []
    for numbers in numbersList:
        data.append(int(numbers.replace('\n>',"")))
    print(np.std(data))
# Perform normality tests
    if ((np.std(data) > 17000) and (np.std(data)<24000)):
        r.sendline(b"1")
        a = r.recvline()
        if a == b'WRONG\n':
            print("1",i)
    else:
        r.sendline(b"0")
        a = r.recvline()
        if a == b'WRONG\n':
            print("0",i)


r.interactive()
r.close()