#Acknowledgements: this project would not have been possible without tutorials and resources from Open CV
import cv2

import numpy as np

from os import listdir

from os.path import isfile, join

path = './faces/'

path_files = [f for f in listdir(path) if isfile(join(path, f))]

Training, Index = [], []

for i, files in enumerate(path_files):

    path_image = path + path_files[i]

    train_images = cv2.imread(path_image, cv2.IMREAD_GRAYSCALE)

    Training.append(np.asarray(train_images, dtype=np.uint8))
 
    Index.append(i)

Index = np.asarray(Index, dtype=np.int32)

face_recognizer = cv2.createLBPHFaceRecognizer()

face_recognizer.train(np.asarray(Training), np.asarray(Index))
print("Training completed successfully")
 
face_detect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

if face_detect.empty():
	raise IOError('Unable to haarcascade_frontalface_default.xml file')

def face_detector(image, size=0.5):
 
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

    face_detection = face_detect.detectMultiScale(gray, 1.3, 5)

    if face_detection is ():
        return image, []
    
    for (x,y,w,h) in face_detection:
		
        cv2.rectangle(image,(x,y),(x+w,y+h),(0,0,255),4)
  
        cropped = image[y:y+h, x:x+w]
        
        cropped = cv2.resize(cropped, (250, 250))
    
    return image, cropped

capture = cv2.VideoCapture(0)

while True:
    # Start capturing frames
	ret, capturing = capture.read()
    
    # Call the function face_detector
	image, faces = face_detector(capturing)
    
	try:
		# cv2.cvtColor: Converts image from one color space to another
		faces = cv2.cvtColor(faces, cv2.COLOR_BGR2GRAY)

		matching = face_recognizer.predict(faces)
        
		if matching[1] < 500:
			score = int( 100 * (1 - (matching[1])/350) )
			string = str(score) + '% Matching Confidence'
        
		if score > 70:
			cv2.putText(image, string, (100, 100), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,255), 2)
			cv2.putText(image, "Access Granted", (210, 40), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,255), 2)

			cv2.imshow('Real-time Face Recognition', image)
		
		else:
			cv2.putText(image, "User Unknown", (150, 100), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255), 3)
			cv2.imshow('Real-time Face Recognition', image)

	except:
		cv2.putText(image, "FACE NOT FOUND", (150, 250) , cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255), 3)
		cv2.imshow('Real-time Face Recognition', image)
		pass
        
	c = cv2.waitKey(1)
	if c == 27:
		break
        
capture.release()

# Close all windows
cv2.destroyAllWindows()     
