#!/usr/bin/env python

import unicornhat as unicorn
from time import sleep


unicorn.set_layout(unicorn.HAT)
unicorn.rotation(0)
unicorn.brightness(0.5)
width,height=unicorn.get_shape()


O = (0, 255, 0) # Green
X = (0, 0, 0) # Black

creeper_pixels = [
    [O, O, O, O, O, O, O, O],
    [O, O, O, O, O, O, O, O],
    [O, X, X, O, O, X, X, O],
    [O, X, X, O, O, X, X, O],
    [O, O, O, X, X, O, O, O],
    [O, O, X, X, X, X, O, O],
    [O, O, X, X, X, X, O, O],
    [O, O, X, O, O, X, O, O]
]

unicorn.set_pixels(creeper_pixels)
unicorn.show()
sleep(5)

