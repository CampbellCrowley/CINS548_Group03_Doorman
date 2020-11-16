#!/usr/bin/python3
# Doorman main app entry point.

from face_recognition import FaceRecognition
from webserver import WebServer
from totp import TOTP
import os

class Doorman:
  """Main Doorman App for the Raspberry Pi."""

  def __init__(self):
    """Begin the app."""

    web_dir = os.path.join(os.path.dirname(__file__), 'html')
    os.chdir(web_dir)
    print('CWD:', web_dir)

    self.totp = TOTP('supersecretkey32') # Key unique to each user.
    self.fr = FaceRecognition()

    self.server = WebServer(8080)
    self.server.set_begin_registration(self.begin_registration)
    self.server.set_verify_code(self.verify_code)

    print('Hello world!')

  def request_unlock(self):
    """Send request to client to unlock the computer."""
    self.server.request_unlock()

  def request_lock(self):
    """Send request to client to lock the computer."""
    self.server.request_lock()

  def begin_registration(self):
    """Handler for web request to register new user."""

    print('Registration beginning!')
    # TODO: Replace this with the registration process.

  def verify_code(self, code):
    """
    Handler for web request to verify the given code.

    :param code: The code to verify from the user.
    :return: True if verified successfully, False if invalid.
    """
    # TODO: Cancel request to lock computer if this is valid.

    is_valid = self.totp.verify_totp(code)
    return is_valid

if __name__ == "__main__":
  Doorman()
