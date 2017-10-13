#!/usr/bin/env python

from time import sleep

from time import sleep

import unicornhat as unicorn


print("""ASCII Pic

You should see a scrolling image, defined in the below variable ASCIIPIC.

If the smiley looks sad, change the rotation from 0 to 180.
""")

unicorn.set_layout(unicorn.HAT)
unicorn.rotation(0)
unicorn.brightness(0.5)
width,height=unicorn.get_shape()

ASCIIPIC=[
     "  XXXX  "
    ," X    X "
    ,"X X  X X"
    ,"X      X"
    ,"X X  X X"
    ,"X  XX  X"
    ," X    X "
    ,"  XXXX  "	
    ]

ASCIIPIC=[
     "  XXXX  "
    ," XXXXXX "
    ,"XX-XX-XX"
    ,"XXXXXXXX"
    ,"XXXXXXXX"
    ,"XX-XX-XX"
    ," XX--XX "
    ,"  XXXX  "	
    ,"        "
    ,"        "
    ,"        "
    ,"        "
    ,"        "
    ,"        "
    ,"        "
    ,"        "
    ]
i = -1

def step():
    global i
    i = 0 if i>=100*len(ASCIIPIC) else i+1 # avoid overflow
    for h in range(height):
        for w in range(width):
            hPos = (i+h) % len(ASCIIPIC)
            chr = ASCIIPIC[hPos][w]
            if chr == ' ':
                unicorn.set_pixel(w, h, 0, 0, 0)
	    elif chr == '-':
                unicorn.set_pixel(w, h, 255, 255, 255)
            else:
                unicorn.set_pixel(w, h, 255, 255, 0)
        unicorn.show()

while True:
    step()
    sleep(0.2)
