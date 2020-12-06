#!/usr/bin/python3
# Doorman main app entry point.
# Author: Campbell Crowley (github@campbellcrowley.com).

from face_recognition import FaceRecognition
from webserver import WebServer
from totp import TOTP
import os
import time

class Doorman:
  """Main Doorman App for the Raspberry Pi."""

  def __init__(self):
    """Begin the app."""

    web_dir = os.path.join(os.path.dirname(__file__), 'html')
    os.chdir(web_dir)
    print('CWD:', web_dir)

    self.totp = TOTP('supersecretkey32') # Key unique to each user.

    self.fr = FaceRecognition()
    self.fr.set_request_unlock(request_unlock)

    self.server = WebServer(port=8080, ws_port=8081)
    self.server.set_begin_registration(self.begin_registration)
    self.server.set_verify_code(self.verify_code)

    self.requestedUnlock = False

    print('Hello world!')

    self.fr.start_recognition()

  def request_unlock(self):
    """Send request to client to unlock the computer."""
    self.server.request_unlock()
    self.requestedUnlock = True
    time.sleep(30)
    if self.requestedUnlock:
      self.request_lock()
      self.requestedUnlock = False

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

    is_valid = self.totp.verify_totp(code)

    self.requestedUnlock = False

    if not is_valid:
      request_lock()

    return is_valid

if __name__ == "__main__":
  Doorman()
