#!/usr/bin/env python

from time import sleep
from sys import exit

try:
    from pyfiglet import figlet_format
except ImportError:
    exit("This script requires the pyfiglet module\nInstall with: sudo pip install pyfiglet")

import unicornhat as unicorn


print("""Figlet

You should see scrolling text that is defined in the TXT variable.

If the text moves in the wrong direction, change the rotation from 0 to 180.

Text output is kind of limited on a pHAT of course because most letters don't
fit on the small display of 4x8.
""")

unicorn.set_layout(unicorn.HAT)
unicorn.rotation(0)
unicorn.brightness(0.5)
width,height=unicorn.get_shape()

print("""Figlet

You should see scrolling text that is defined in the TXT variable.

If the text moves in the wrong direction, change the rotation from 0 to 180.

Text output is kind of limited on a pHAT of course because most letters don't
fit on the small display of 4x8.
""")

width = 8
height = 8

TXT = "HELLO WORLD !!!"
TXT = "One small step for man, One giant leap for man-kind."
TXT = "Linux Pratique forever!!!"

figletText = figlet_format(TXT+' ', "banner4", width=1000) # banner font generates text with heigth 7
figletText = figlet_format(TXT+' ', "3x5", width=1000) # banner font generates text with heigth 7
figletText = figlet_format(TXT+' ', "3-d", width=1000) # banner font generates text with heigth 7
figletText = figlet_format(TXT+' ', "alligator", width=1000) # banner font generates text with heigth 7
figletText = figlet_format(TXT+' ', "alligator2", width=1000) # banner font generates text with heigth 7
figletText = figlet_format(TXT+' ', "contrast", width=1000) # banner font generates text with heigth 7
figletText = figlet_format(TXT+' ', "marquee", width=1000) # banner font generates text with heigth 7
figletText = figlet_format(TXT+' ', "o8", width=1000) # banner font generates text with heigth 7
figletText = figlet_format(TXT+' ', "sblood", width=1000) # banner font generates text with heigth 7
figletText = figlet_format(TXT+' ', "starwars", width=1000) # banner font generates text with heigth 7
figletText = figlet_format(TXT+' ', "stellar", width=1000) # banner font generates text with heigth 7
figletText = figlet_format(TXT+' ', "univers", width=1000) # banner font generates text with heigth 7
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

#print(len(figletText))
#print(textMatrix)
#print(len(textMatrix))
#print(textWidth)


unicorn.clear()

while True:
	for i in range (0, 1*textWidth-8):
	    step()
	    sleep(0.04)

unicorn.clear()
