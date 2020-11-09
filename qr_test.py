#!/usr/bin/python3

# Need to install 2 libraries:
# `pip3 install qrcode[pil]`
# and
# `pip3 install pyotp`

import pyotp
import qrcode

secret = 'base32secret3232'

totp = pyotp.totp.TOTP(secret)

print('Email: ', end='')
email = input()

uri = totp.provisioning_uri(name=email, issuer_name='Doorman')

img = qrcode.make(uri)
img.show('code.png')
# img.save('code.png')

print('Enter Code: ', end='')
test = input()
if totp.verify(test):
  print('Success!')
else:
  print('Fail!')
