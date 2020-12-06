# Author: Campbell Crowley (github@campbellcrowley.com).
import pyotp
import qrcode

class TOTP:
  """
  Time based One Time Passcode generation API for Doorman.
  """

  def __init__(self, secret, app_name='Doorman'):
    """
    Create TOTP helper for a single user.

    :param secret: The secret key for a single user.
    :param app_name: The app name to display to a user when registering for TOTP.
    :return: nothing.
    """
    self.secret = secret
    self.app_name = app_name

    self.totp = pyotp.totp.TOTP(self.secret)

  def get_uri(self, email):
    """
    Get the URI for generating a QR Code to create a profile on Authy or Google
    Authenticator.

    :param email: Email of the user requesting to register.
    :return: string URI to turn into a QR Code.
    """
    return self.totp.provisioning_uri(name=email, issuer_name=self.app_name)

  def get_qr_code(self, email):
    """
    Get the QR code to scan into auth app for user profile creation.

    :param email: Email of the user requesting to register with auth app.
    :return: Generated image.
    """
    return self.uri_to_qr(get_uri(email))

  def uri_to_qr(self, uri):
    """
    Convert a URI to a QR Code.

    :param uri: The URI to convert.
    :return: Generated image.
    """
    return qrcode.make(uri)

  def verify_totp(self, code):
    """
    Verify a TOTP code from the authenticator app for the current user.

    :param code: The 6-digit code from the auth app.
    :return: True if verified, False if invalid.
    """
    return self.totp.verify(code)
