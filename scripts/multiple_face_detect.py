import cv2
from deepface import DeepFace


class FaceDetection:
    def __init__(self) -> None:
        pass

    def convert_to_grayscale(self, image_path):
        # Convert the BGR image into grayscale
        image = cv2.imread(image_path)
        return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    def detect_faces(self, image_path):
        gray = self.convert_to_grayscale(image_path)
        #cv2.imwrite("black-white.png", gray)
        """faceCascade = cv2.CascadeClassifier(
            cv2.data.haarcascades + "haarcascade_frontalface_default.xml")"""
        
        faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_profileface.xml")
        
        faces = faceCascade.detectMultiScale(
            gray, scaleFactor=1.3, minNeighbors=3, minSize=(60, 60))
        return faces

    def draw_box_faces(self, faces, image_path):
        image = cv2.imread(image_path)
        for (x, y, w, h) in faces:
            cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
            print("Face found. Saving Locally!!")
            roi_color = image[y: y+h, x:x+w]
            cv2.imwrite(str(w) + str(h) + '_faces.jpg', roi_color)

    def get_face_analysis(self, image_path):
        analysis = DeepFace.analyze(image_path, actions = ['age', 'gender', 'race', 'emotion'], enforce_detection=False)
        # analysis is a dictionary object
        return analysis