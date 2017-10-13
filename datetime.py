#!/usr/bin/env python

import os
import time
from time import sleep
import datetime

try:
    from pyfiglet import figlet_format
except ImportError:
    exit("This script requires the pyfiglet module\nInstall with: sudo pip install pyfiglet")

import unicornhat as unicorn

unicorn.set_layout(unicorn.HAT)
unicorn.rotation(180)
unicorn.brightness(0.5)
width,height=unicorn.get_shape()

#print("Setting time")
#bashCommand = "sudo service ntp stop; sudo ntpdate 193.50.119.254; sudo service ntp start"
#os.system(bashCommand)
now = datetime.datetime.now()
print(now)
#print("Ok")
TXT = now.strftime("Date : %d %B %Y ")+now.strftime("Heure : %H:%M")
print(TXT)
#figletText = figlet_format(TXT+' ', "banner4", width=1000) # banner font generates text with heigth 7
#figletText = figlet_format(TXT+' ', "3x5", width=1000) # banner font generates text with heigth 7
#figletText = figlet_format(TXT+' ', "3-d", width=1000) # banner font generates text with heigth 7
#figletText = figlet_format(TXT+' ', "alligator", width=1000) # banner font generates text with heigth 7
#figletText = figlet_format(TXT+' ', "alligator2", width=1000) # banner font generates text with heigth 7
#figletText = figlet_format(TXT+' ', "contrast", width=1000) # banner font generates text with heigth 7
#figletText = figlet_format(TXT+' ', "marquee", width=1000) # banner font generates text with heigth 7
#figletText = figlet_format(TXT+' ', "o8", width=1000) # banner font generates text with heigth 7
#figletText = figlet_format(TXT+' ', "sblood", width=1000) # banner font generates text with heigth 7
#figletText = figlet_format(TXT+' ', "starwars", width=1000) # banner font generates text with heigth 7
#figletText = figlet_format(TXT+' ', "stellar", width=1000) # banner font generates text with heigth 7
#figletText = figlet_format(TXT+' ', "univers", width=1000) # banner font generates text with heigth 7
figletText = figlet_format(TXT+' ', "3-d", width=1000) # banner font generates text with heigth 7
print(figletText)
textMatrix = figletText.split("\n")[:width] # width should be 8 on both HAT and pHAT!
textHeight = len(textMatrix)
if textMatrix[textHeight-1]=='':
	textHeight = textHeight -1
textWidth = len(textMatrix[0]) # the total length of the result from figlet
i = -1

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

print(len(figletText))
print(textMatrix)
print(len(textMatrix))
print(textWidth)

unicorn.clear()
while True:
    now = datetime.datetime.now()
    TXT = now.strftime("Date : %d %B %Y ")+now.strftime("Heure : %H:%M")
    print(TXT)
    figletText = figlet_format(TXT+' ', "3-d", width=1000) # banner font generates text with heigth 7
    textMatrix = figletText.split("\n")[:width] # width should be 8 on both HAT and pHAT!
    textHeight = len(textMatrix)
    if textMatrix[textHeight-1]=='':
        textHeight = textHeight -1
    textWidth = len(textMatrix[0]) # the total length of the result from figlet
    for i in range (0, 1*textWidth-8):
        step()
        sleep(0.04)

unicorn.clear()

