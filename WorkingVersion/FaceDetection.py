#Acknowledgements: this project would not have been possible without tutorials and resources from Open CV
import cv2

import numpy as np

face_detect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

if face_detect.empty():
	raise IOError('Unable to haarcascade_frontalface_default.xml file')
 
def face_detector(image):

    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

    face_detection = face_detect.detectMultiScale(gray, 1.3, 5)
    
    if face_detection is ():
        return None

    for (x,y,w,h) in face_detection:
        face_cropped = image[y:y+h, x:x+w]

    return face_cropped

capture = cv2.VideoCapture(0)

face_count = 0

while True:
	ret, capturing = capture.read()
	
	if face_detector(capturing) is not None:
		face_count += 1

		resized_frame = cv2.resize(face_detector(capturing), (250, 250))
		
		gray = cv2.cvtColor(resized_frame, cv2.COLOR_BGR2GRAY)

		path = './faces/' + str(face_count) + '.jpg'
		
		cv2.imwrite(path, gray)
		
		cv2.putText(gray, str(face_count), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 2)
		
		cv2.imshow('Cropped', gray)
        
	else:
		print("Face NOT detected")
		pass

	if cv2.waitKey(1) == 27 or face_count == 20: # 27 is the Esc Key
		break
        
capture.release()

cv2.destroyAllWindows()
