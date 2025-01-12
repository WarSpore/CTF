import sys

import numpy
import matplotlib.pyplot as plt
from PIL import Image
import random

def get_rand(x):
	def _random():
		nonlocal x
		x ^= (x << 14) & 0xFFFFFFFF
		x ^= (x >> 6) & 0xFFFFFFFF
		x ^= (x << 11) & 0xFFFFFFFF
		return x & 0xFF
	return _random


def encrypt(in_img, key):
	in_img = "test"
	height = len(in_img)*3
	width = len(in_img)*3
	rand = get_rand(key)
	
	for y in range(height):
		for x in range(width):
			 print(bin(rand()),x)
		

if __name__=='__main__':
	IN_IMG = "s"*32
	KEY = random.getrandbits(32)
	print(bin(KEY))
	encrypt(IN_IMG, KEY)