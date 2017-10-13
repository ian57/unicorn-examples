from sense_hat import SenseHat
import time

sense = SenseHat()

X = [255, 0, 0]  # Red
O = [255, 255, 255]  # White

question_mark = [
O, O, O, X, X, O, O, O,
O, O, X, O, O, X, O, O,
O, O, O, O, O, X, O, O,
O, O, O, O, X, O, O, O,
O, O, O, X, O, O, O, O,
O, O, O, X, O, O, O, O,
O, O, O, O, O, O, O, O,
O, O, O, X, O, O, O, O
]

sense.set_pixels(question_mark)
time.sleep(5) # delays for 5 seconds
sense.clear()  # no arguments defaults to off

sense.clear(255, 127, 0)

print(sense.gamma)
time.sleep(2)

sense.gamma = list(reversed(sense.gamma))
print(sense.gamma)
time.sleep(2)

sense.low_light = True
print(sense.gamma)
time.sleep(2)

sense.low_light = False
time.sleep(2)
sense.clear()  # no arguments defaults to off
