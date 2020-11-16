#!/usr/bin/python3
# Doorman main app entry point.

from .face_recognition import FaceRecognition
from .totp import TOTP

def main():
  totp = TOTP('supersecretkey32') # Key unique to each user.
  fr = FaceRecognition()

  print('Hello world!')

if __name__ == "__main__":
  main()
