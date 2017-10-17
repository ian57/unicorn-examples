#!/usr/bin/env python

import unicornhat as unicorn
import time
from var_dump import var_dump
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

def animateSpriteOld(sprite,delay=0.1):
	for index,spr in enumerate(sprite):
        	unicorn.set_pixels(spr)
                unicorn.show()
	        time.sleep(delay)

def animateSprite(sprite,delay,direction):
        if (len(sprite)!=0):
                for index,spr in enumerate(sprite):
                        if direction=='b':
                                #unicorn.set_pixels(list(reversed(spr)))
				for sublist in spr:
                                        sublist.reverse()
                        unicorn.set_pixels(spr)
                	unicorn.show()  
		        time.sleep(delay)
        else:
                unicorn.clear()         
      		unicorn.show()  
                time.sleep(delay)

unicorn.set_layout(unicorn.HAT)
unicorn.rotation(0)
unicorn.brightness(0.5)
width,height=unicorn.get_shape()

none=[]
skulls = readSprites('sprites/skulls.png')
clyde = readSprites('sprites/clyde-sheet.png')
blinky = readSprites('sprites/blinky-sheet.png')
inky = readSprites('sprites/inky-sheet.png')
deadghost = readSprites('sprites/deadghost-sheet.png')
pinky = readSprites('sprites/pinky-sheet.png')
pacman = readSprites('sprites/pacman-sheet.png')

animation_order = [[pacman, 0.12, 'f'], [none,0.8,'f'] , [clyde,0.1,'f'], [none,0.8,'f'], [deadghost, 0.03, 'b'], [none,0.5,'f'], [pacman, 0.03, 'b']]

for i in range (len(animation_order)):
        [animation,delay,direction] = animation_order.pop(0)
        animateSprite(animation,delay,direction)
        animation_order.append(animation)

unicorn.clear()
