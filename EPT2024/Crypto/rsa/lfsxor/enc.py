import sys

import numpy
import matplotlib.pyplot as plt
from PIL import Image


def get_rand(x):
	def _random():
		nonlocal x
		x ^= (x << 14) & 0xFFFFFFFF
		x ^= (x >> 6) & 0xFFFFFFFF
		x ^= (x << 11) & 0xFFFFFFFF
		return x & 0xFF
	return _random


def encrypt(in_img, out_img, key):
	in_img = plt.imread(in_img)[:, :, 0]
	height = len(in_img)
	width = len(in_img[0])
	
	imarr = numpy.zeros((height, width, 3), dtype='uint8')
	rand = get_rand(key)
	
	for y in range(height):
		for x in range(width):
			imarr[y,x] = int(in_img[y,x] ^ rand())
	
	im = Image.fromarray(imarr.astype('uint8')).convert('RGB')
	im.save(out_img)


if __name__=='__main__':
	IN_IMG = sys.argv[1]
	OUT_IMG = sys.argv[2]
	KEY = int(sys.argv[3])
	encrypt(IN_IMG, OUT_IMG, KEY)