from Led import *
from Constants import *


class FaceLock:
    def __init__(self):
        print ("start main")
        self.green_led = Led(GREEN)
        self.yellow_led = Led(YELLOW)
        self.red_led = Led(RED)
        self.detected = False

    def run(self):
        if self.detect() == True:
            self.unlock()
            self.green_led.on()
        else:
            self.lock()
            self.red_led.on()

    def detect(self):
        return False

    def failure(self):
        self.red_led.blink()

    def pending(self):
        self.yellow_led.on()

    def complete(self):
        self.yellow_led.off()

    def access(self):
        self.green_led.on()

    def lock(self):
        print("Locked")

    def unlock(self):
        print("Unlocked")


while input_state == True:
    system.run()
    system.events()