#!/usr/bin/env python

import unicornhat as unicorn
import time
import signal
from sys import exit

try:
    from PIL import Image
except ImportError:
    exit("This script requires the pillow module\nInstall with: sudo pip install pillow")

def readSprites(filename):
	img = Image.open(filename)
	sprites_list = []
	for o_x in range(int(img.size[0]/8)):
	    for o_y in range(int(img.size[1]/8)):
	        sprite=[]
	        for x in range(8):
                    row=[]
        	    for y in range(8):
                	pixel = img.getpixel(((o_x*8)+y,(o_y*8)+x))
        	        r, g, b = int(pixel[0]),int(pixel[1]),int(pixel[2])
                        row.append([r,g,b])
                    sprite.append(row)
	        sprites_list.append(sprite)
	return sprites_list

def animateSprite(sprite,delay=0.1):
	for index,spr in enumerate(sprite):
        	unicorn.set_pixels(spr)
                unicorn.show()
	        time.sleep(delay)

unicorn.set_layout(unicorn.HAT)
unicorn.rotation(0)
unicorn.brightness(0.5)
width,height=unicorn.get_shape()

sprite1 = readSprites('sprites/skulls.png')
sprite2 = readSprites('sprites/clyde-sheet.png')
sprite3 = readSprites('sprites/pacmanb-sheet.png')

animateSprite(sprite1)
animateSprite(sprite2,0.05)


for index,spr in enumerate(sprite3):
	unicorn.set_pixels(spr)
        unicorn.show()
	time.sleep(0.1)
unicorn.clear()
