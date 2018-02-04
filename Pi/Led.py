import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)


class Led:
    def __init__(self, colour):
        print ("initialise led")
        self.pin = colour
        self.count = 1
        GPIO.setup(self.pin, GPIO.OUT)

    def blink(self):
        while self.count <= 4:
            print ("blink led")
            GPIO.output(self.pin, GPIO.HIGH)
            time.sleep(0.15)
            GPIO.output(self.pin, GPIO.LOW)
            time.sleep(0.15)
            self.count += 1
        GPIO.cleanup()

    def on(self):
        'GPIO.setup(self.pin, GPIO.OUT)'
        'GPIO.setup(self.pin, GPIO.OUT)'
        GPIO.output(self.pin, GPIO.HIGH)

    def off(self):
        'GPIO.setup(self.pin, GPIO.OUT)'
        'GPIO.setup(self.pin, GPIO.OUT)'
        GPIO.output(self.pin, GPIO.LOW)