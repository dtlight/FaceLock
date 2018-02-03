from Led import *
from Constants import *


class Main:
    def __init__(self):
        print ("start main")
        self.green_led = Led(GREEN)
        self.yellow_led = Led(YELLOW)
        self.red_led = Led(RED)

    def run(self):
        if 1 < 2:
            self.red_led.blink()

    def blink(self, led):
        led.blink()


pi = Main()

while True:
    pi.run()
