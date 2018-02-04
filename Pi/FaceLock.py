from Led import *
from Constants import *
import face_recognition
import os

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
        image = face_recognition.load_image_file("../Server/app/static/images/temp/unknown.jpg")
        self.recognise(image)

    def failure(self):
        self.red_led.blink()

    def recognise(self, image):
        for filename in os.listdir("../Server/app/static/images/face"):
            if filename.endswith(".jpg"):
                print(os.path.join("../Server/app/static/images/face", filename))
                continue
            else:
                continue

        face_encoding = face_recognition.face_encodings(image)[0]
        for photo in photos:
            results = face_recognition.compare_faces([face_encoding], unknown_face_encoding)

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
