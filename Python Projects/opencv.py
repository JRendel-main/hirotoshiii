import cv2

cam = cv2.VideoCapture(1)
cam.set(3,640)
cam.set(4,480)

while True:
	sucess, img = cam.read()

face_cascade = cv2.CascadeClassifier('face_detector.xml')
img = cv2.imread(img)
faces = face_cascade.detectMultiScale(img, 1.1, 4)
for (x, y, w, h) in faces: 
	cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
	cv2.imwrite('saved.png', img) 
	print('Successfully saved')