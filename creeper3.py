#!/usr/bin/env python

import unicornhat as unicorn
from time import sleep
try:
    from PIL import Image
except ImportError:
    exit("This script requires the pillow module\nInstall with: sudo pip install pillow")

def readImage(filename):
    img = Image.open(filename)
    image=[]
    for x in range(8):
	row=[]
        for y in range(8):
            pixel = img.getpixel((y,x))
            r, g, b = int(pixel[0]),int(pixel[1]),int(pixel[2])
            row.append([r,g,b])
        image.append(row)
    return image

unicorn.set_layout(unicorn.HAT)
unicorn.rotation(0)
unicorn.brightness(0.5)
width,height=unicorn.get_shape()

creeper = readImage("sprites/creeper.png")
#print creeper
unicorn.set_pixels(creeper)
unicorn.show()
sleep(5)
