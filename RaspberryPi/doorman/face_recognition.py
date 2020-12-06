# Authors: Campbell Crowley (github@campbellcrowley.com) & Kyle Crowley.
import face_recognition
import cv2
import picamera
import numpy as np

def undefined_func(self):
  raise Exception('Function not defined!')
request_unlock = undefined_func

class FaceRecognition:
  """
  Face recognition and identification for Doorman.
  """

  def __init__(self):
    print('Face Recognition!')

    self.webcam = cv2.VideoCapture(0)
    #load the default user face encoding
    image = face_recognition.load_image_file("User.jpg")
    userEncoding = face_recognition.face_encodings(image)[0]

    self.knownFaceEncodings = [
        userEncoding
    ]
    self.isRunning = True

  def shutdown(self):
    print("FaceRecognition Shutting Down")
    self.isRunning = False

  def set_request_unlock(self, func):
    global request_unlock
    request_unlock = func

  def start_recognition(self):
    faceLocations = []
    faceEncodings = []
    processThisFrame = True
    self.isRunning = True

    lastMatched = False

    while self.isRunning:
        ret, frame = self.webcam.read()
        smallFrame = cv2.resize(frame,(0,0),fx=0.25,fy=0.25)
        rgbSmallFrame = smallFrame[:,:,::-1]

        if processThisFrame:
            #find all faces in frame and encode them
            faceLocations = face_recognition.face_locations(rgbSmallFrame)
            faceEncodings = face_recognition.face_encodings(rgbSmallFrame,faceLocations)

            for face_encoding in faceEncodings:
                matches = face_recognition.commpare_faces(knownFaceEncodings,face_encoding)

            if True in matches:
              if not lastMatched:
                request_unlock()
              lastMatched = True
            else:
              lastMatched = False

            processThisFrame = not processThisFrame

        #hit q to quit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    VideoCapture.release()
    cv2.destroyAllWindows()
