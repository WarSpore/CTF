from pwn import *
from itertools import permutations



colors = ["red", "blue", "green", "yellow"]
foods = ["pizza", "pasta", "steak", "chicken"]

# Generate all possible permutations of colors and foods
color_permutations = permutations(colors)
food_permutations = permutations(foods)

for color_permutation in color_permutations:
    for food_permutation in food_permutations:
        r = remote("babyrevjohnson.chal.irisc.tf", 10002)
        r.recvuntil("color:")
        for color in color_permutation:
            r.sendline(color)
        for food in food_permutation:
            r.sendline(food)
        sleep(0.5)
        print(r.recvuntil('\n'))
        print(r.close())
