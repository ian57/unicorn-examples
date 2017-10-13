from sense_hat import SenseHat
import time
import datetime

sense = SenseHat()

sense.set_rotation(180)

blue = sense.load_image("sprites/deadghost8.png", redraw=False)
sense.set_pixels(blue)

