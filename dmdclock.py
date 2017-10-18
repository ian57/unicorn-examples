#!/usr/bin/python

#!/usr/bin/env python

import unicornhat as unicorn
import time
import signal
from sys import exit

try:
    from PIL import Image
except ImportError:
    exit("This script requires the pillow module\nInstall with: sudo pip install pillow")

try:
    from pyfiglet import figlet_format
except ImportError:
    exit("This script requires the pyfiglet module\nInstall with: sudo pip install pyfiglet")

import os
import datetime
import locale

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

def step():
    global i
    i = 0 if i>=100*textWidth else i+1 # avoid overflow
    for h in range(height):
        #for w in range(width):
        for w in range(textHeight):
            hPos = (i+h) % textWidth
	    #print(h,' ',w,' ',hPos,)
            chr = textMatrix[w][hPos]
	    #print(h,' ',w,' ',hPos,' ',chr)
	    if chr in ['/', '\\', '_', '(',')','d','8','P', 'b', 'Y', '8','o', '^', '|', '-', '`', 'a', '"' ]:
                unicorn.set_pixel(width-w-1, h, 255, 255, 255)
            elif chr == '#':
                unicorn.set_pixel(width-w-1, h, 255, 0, 0)
            elif chr == '*':
                unicorn.set_pixel(width-w-1, h, 255, 0, 0)
            elif chr == ':':
		unicorn.set_pixel(width-w-1, h, 255, 255, 255)
            elif chr == '.':
		unicorn.set_pixel(width-w-1, h, 128, 255, 128)
            elif chr == '+':
		unicorn.set_pixel(width-w-1, h, 255, 0, 255)
            elif chr == '@':
		unicorn.set_pixel(width-w-1, h, 255, 0, 0 )
            elif chr == '!':
		unicorn.set_pixel(width-w-1, h, 255, 128, 128)
            elif chr == '\'':
		unicorn.set_pixel(width-w-1, h, 255, 0, 128)
	    else:
                unicorn.set_pixel(width-w-1, h, 0, 0, 0)
	unicorn.show()



# Let's set a non-US locale
locale.setlocale(locale.LC_TIME, "fr_FR.UTF8")
#print("Setting time")
#bashCommand = "sudo service ntp stop; sudo ntpdate 193.50.119.254; sudo service ntp start"
#os.system(bashCommand)
now = datetime.datetime.now()
print(now.strftime("Date : %d %B %Y Heure : %H:%M"))

none=[]
clyde = readSprites('sprites/clyde-sheet.png')
blinky = readSprites('sprites/blinky-sheet.png')
inky = readSprites('sprites/inky-sheet.png')
deadghost = readSprites('sprites/deadghost-sheet.png')
pinky = readSprites('sprites/pinky-sheet.png')
pacman = readSprites('sprites/pacman-sheet.png')

TXT=now.strftime("Date : %d %B %Y ")+now.strftime("Heure : %H:%M")
figletText = figlet_format(TXT+' ', "3-d", width=1000) # banner font generates text with heigth 7
print(figletText)
textMatrix = figletText.split("\n")[:width] # width should be 8 on both HAT and pHAT!
textHeight = len(textMatrix)
if textMatrix[textHeight-1]=='':
	textHeight = textHeight -1
textWidth = len(textMatrix[0]) # the total length of the result from figlet
i = -1


while (True):
	animateSprite(pacman,0.1,'f')
	animateSprite(none,0.7,'f')
	now = datetime.datetime.now()
        TXT = now.strftime(" Date : %d %B %Y ")
        figletText = figlet_format(TXT+' ', "3-d", width=1000) # banner font generates text with heigth 7
        textMatrix = figletText.split("\n")[:width] # width should be 8 on both HAT and pHAT!
        textHeight = len(textMatrix)
        if textMatrix[textHeight-1]=='':
            textHeight = textHeight -1
        textWidth = len(textMatrix[0]) # the total length of the result from figlet
        unicorn.rotation(270)
        for i in range (0, 1*textWidth-8):
            step()
            time.sleep(0.04)
        unicorn.rotation(0)
	animateSprite(none,0.7,'f')
	animateSprite(pacman,0.1,'b')
	animateSprite(none,0.7,'f')
	animateSprite(inky,0.1,'b')
	animateSprite(none,0.7,'f')
        TXT = now.strftime(" Heure : %H:%M ")
        figletText = figlet_format(TXT+' ', "3-d", width=1000) # banner font generates text with heigth 7
        textMatrix = figletText.split("\n")[:width] # width should be 8 on both HAT and pHAT!
        textHeight = len(textMatrix)
        if textMatrix[textHeight-1]=='':
            textHeight = textHeight -1
        textWidth = len(textMatrix[0]) # the total length of the result from figlet
        unicorn.rotation(270)
        for i in range (0, 1*textWidth-8):
            step()
            time.sleep(0.04)
        unicorn.rotation(0)
        animateSprite(none,0.7,'f')
	animateSprite(inky,0.1,'f')
	animateSprite(none,0.7,'f')
        animateSprite(clyde,0.1,'b')
        animateSprite(none,0.7,'f')
        TXT = " Liunux Pratique Forever!!! "
        figletText = figlet_format(TXT+' ', "3-d", width=1000) # banner font generates text with heigth 7
        textMatrix = figletText.split("\n")[:width] # width should be 8 on both HAT and pHAT!
        textHeight = len(textMatrix)
        if textMatrix[textHeight-1]=='':
            textHeight = textHeight -1
        textWidth = len(textMatrix[0]) # the total length of the result from figlet
        unicorn.rotation(270)
        for i in range (0, 1*textWidth-8):
            step()
            time.sleep(0.04)
        unicorn.rotation(0)
        animateSprite(none,0.7,'f')
        animateSprite(clyde,0.1,'f')
        animateSprite(none,0.7,'f')




