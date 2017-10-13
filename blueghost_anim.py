from sense_hat import SenseHat
import time
import datetime

sense = SenseHat()

sense.set_rotation(180)

blue_mov1 = sense.load_image("sprites/deadghost1.png", redraw=False)
blue_mov2 = sense.load_image("sprites/deadghost2.png", redraw=False)
blue_mov3 = sense.load_image("sprites/deadghost3.png", redraw=False)
blue_mov4 = sense.load_image("sprites/deadghost4.png", redraw=False)
blue_mov5 = sense.load_image("sprites/deadghost5.png", redraw=False)
blue_mov6 = sense.load_image("sprites/deadghost6.png", redraw=False)
blue_mov7 = sense.load_image("sprites/deadghost7.png", redraw=False)
blue_mov8 = sense.load_image("sprites/deadghost8.png", redraw=False)
blue_mov9 = sense.load_image("sprites/deadghost9.png", redraw=False)
blue_mov10 = sense.load_image("sprites/deadghost10.png", redraw=False)
blue_mov11 = sense.load_image("sprites/deadghost11.png", redraw=False)
blue_mov12 = sense.load_image("sprites/deadghost12.png", redraw=False)
blue_mov13 = sense.load_image("sprites/deadghost13.png", redraw=False)
blue_mov14 = sense.load_image("sprites/deadghost14.png", redraw=False)
blue_mov15 = sense.load_image("sprites/deadghost15.png", redraw=False)


def blue_mov(direction):
        if direction:
		sprites = [blue_mov1, blue_mov2, blue_mov3, blue_mov4, blue_mov5, blue_mov6, blue_mov7, blue_mov8, blue_mov9, blue_mov10, blue_mov11, blue_mov12, blue_mov13, blue_mov14, blue_mov15]
        else:
		sprites = [blue_mov15, blue_mov14, blue_mov13, blue_mov12, blue_mov11, blue_mov10, blue_mov9, blue_mov8, blue_mov7, blue_mov6, blue_mov5, blue_mov4, blue_mov3, blue_mov2, blue_mov1]
        for sprite in sprites:
                sense.set_pixels(sprite)
                time.sleep(0.1) # delays for 100 miliseconds

blue_mov(1)
sense.clear()  # no arguments defaults to off
time.sleep(1)
blue_mov(0)
sense.clear()  # no arguments defaults to off
time.sleep(1)

