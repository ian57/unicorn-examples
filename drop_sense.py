#!/usr/bin/env python

import time
from random import randint

from sense_hat import SenseHat

sense = SenseHat()
sense.set_rotation(0)
sense.low_light = True


print("""Drop

Creates a virtual bucket and fills it with randomly coloured dots.

If you're using a Unicorn HAT and only half the screen lights up, 
edit this example and  change 'unicorn.AUTO' to 'unicorn.HAT' below.
""")

uh_width = 8
uh_height = 8

heights = []

def setup():

    global heights
    heights = []
    for b in range(0, (uh_width-2)):
        heights.append(0)
    sense.clear()
    for b in range(0, uh_height):
        sense.set_pixel(0, b, 255, 255, 255)
    for b in range(0, uh_height):
        sense.set_pixel((uh_width-1), b, 255, 255, 255)
    for b in range(1, (uh_width-1)):
        sense.set_pixel(b, 0, 255, 255, 255)

def drop_ball():

    ball_colour = [randint(100, 255), randint(100, 255), randint(100, 255)]
    ball_column = randint(0, (uh_width-3))

    while heights[ball_column] == (uh_height-1):
        ball_column = randint(0, (uh_width-3))
    height = heights[ball_column]
    ball_y = (uh_height-1)
    sense.set_pixel(ball_column + 1, ball_y, ball_colour[0], ball_colour[1], ball_colour[2])
    dropcount = (uh_height-2) - height
    for y in range(0, dropcount):
        sense.set_pixel(ball_column + 1, ball_y, 0, 0, 0)
        ball_y -= 1
        sense.set_pixel(ball_column + 1, ball_y, ball_colour[0], ball_colour[1], ball_colour[2])
        time.sleep(0.02)
    heights[ball_column] += 1


setup()
while True:
    for i in range(0, (uh_width-2)*(uh_height-1)):
        drop_ball()
    time.sleep(1)
    setup()

