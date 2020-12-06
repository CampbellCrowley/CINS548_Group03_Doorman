#!/usr/bin/env python3
# Author: Campbell Crowley (github@campbellcrowley.com).
# Doorman windows app entry point.
import WinClient
from webclient import WebClient

pi_address = 'raspberrypi.local'
# pi_address = 'localhost'

class Doorman:
  """The Windows client side of Doorman."""

  def __init__(self):
    self.app = WinClient
    self.client = WebClient(8081, pi_address)
    self.client.set_lock_handler(self.lock_handler)
    self.client.set_unlock_handler(self.unlock_handler)
    self.client.start()

    print('Hello World!')

  def unlock_handler(self):
    """Handle request from server to unlock computer."""
    print("Unlock requested!")
    self.app.autounlock()

  def lock_handler(self):
    """Handle request to lock computer."""
    print("Lock requested!")
    # TODO: Call lock function.

if __name__ == "__main__":
  Doorman()
