import face_recognition
import cv2
import picamera
import numpy as np

webcam = cv2.VideoCapture(0)

knownFaceEncodings = [

]

knownFaceNames = [
    "User",
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
        #find all faces in frame and encode them
        faceLocations = face_recognition.face_locations(rgbSmallFrame)
        faceEncodings = face_recognition.face_encodings(rgbSmallFrame,faceLocations)
        faceNames = []
        #add all faces to known face encoding list
        knownFaceEncodings.append(faceEncodings)

        processThisFrame = not processThisFrame

    #hit q to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

VideoCapture.release()
cv2.destroyAllWindows()
