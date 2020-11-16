import face_recognition
import cv2

webcam = cv2.VideoCapture(0)

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
            name = "Unknown"

            if True in matches:
                firstMatchIndex = matches.index(true)
                name = knownFaceNames[firstMatchIndex]

            faceNames.append(name)

        processThisFrame = not processThisFrame

        for (top,right,bottom,left), name in zip(faceLocations, faceNames):
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4

            cv2.rectangle(frame,(left,top), (right,bottom), (0,0,255), 2)

            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

        cv2.imshow('Video', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

VideoCapture.release()
cv2.destroyAllWindows()
