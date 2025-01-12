import sys
import numpy
import matplotlib.pyplot as plt
from PIL import Image

def decrypt(in_img):
    in_img = plt.imread(in_img)[:, :, 0]
    height = len(in_img)
    width = len(in_img[0])
    
    imarr = numpy.zeros((height, width, 3), dtype='uint8')
    for i in range(256):
        for y in range(height):
            for x in range(width):
                imarr[y, x] = int(in_img[y, x] ^ i)
        
        im = Image.fromarray(imarr.astype('uint8')).convert('RGB')
        #im.save(f"EPT2024\\Crypto\\rsa\\lfsxor\\out{i}.bmp")

if __name__ == '__main__':
    IN_IMG = "EPT2024\\Crypto\\rsa\\lfsxor\\out.bmp"
    decrypt(IN_IMG)
