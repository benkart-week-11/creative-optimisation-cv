import cv2
import sys
from deepface import DeepFace

# The path of the image is passed as an argument during runtime
image_path = sys.argv[1]

#Convert the BGR image into grayscale
image = cv2.imread(image_path)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.3,
    minNeighbors=3,
    minSize=(60,60)
)

print("Found {0} Faces!!".format(len(faces)))

for (x, y, w, h) in faces:
    cv2.rectangle(image, (x,y), (x+w, y+h), (0,255,0), 2)
    print("Object found. Saving Locally!!")
    roi_color = image[y: y+h, x:x+w]
    cv2.imwrite(str(w) + str(h) + '_faces.jpg', roi_color)

image_path="Required Image Path"
analyze = DeepFace.analyze(cv2.imread(image_path), actions=['emotions'])
print(analyze["dominanmt_emotion"])


status = cv2.imwrite('face_detected.jpg', image)

print ("Image faces_detected.jpg written to filesystem: ",status)

