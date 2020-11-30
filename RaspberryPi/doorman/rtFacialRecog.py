import face_recognition
import cv2
import picamera
import numpy as np

webcam = cv2.VideoCapture(0)

#load the default user face encoding
image = face_recognition.load_image_file("User.jpg")
userEncoding = face_recognition.face_encodings(image)[0]

knownFaceEncodings = [

]

knownFaceNames = [

]

faceLocations = []
faceEncodings = []
faceNames = []
processThisFrame = True

while True:
    ret, frame = webcam.read()
    smallFrame = cv2.resize(frame,(0,0),fx=0.25,fy=0.25)
    rgbSmallFrame = smallFrame[:,:,::-1]

    if processThisFrame:
        faceLocations = face_recognition.face_locations(rgbSmallFrame)
        faceEncodings = face_recognition.face_encodings(rgbSmallFrame,faceLocations)
        faceNames = []

        for face_encoding in faceEncodings:
            matches = face_recognition.commpare_faces(knownFaceEncodings,face_encoding)

            if True in matches:
                return True

        processThisFrame = not processThisFrame


        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

VideoCapture.release()
cv2.destroyAllWindows()

