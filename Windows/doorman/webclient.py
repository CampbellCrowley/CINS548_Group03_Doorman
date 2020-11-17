import websockets
import asyncio
import threading

def undefined_func():
  raise Exception("Undefined Function!")

unlock_handler = undefined_func
lock_handler = undefined_func

class WebClient:
  """Doorman Webclient for communicating with server."""

  def __init__(self, port=81, host='localhost'):
    """
    Create and start Doorman webserver.

    :param port: Port to listen on.
    :param addr: Address to listen on.
    :return: Nothing.
    """

    self.uri = f"ws://{host}:{port}"

    self.alive = True
    self.socket = None

  def start(self):
    print("Starting web client:", self.uri)
    self.alive = True
    asyncio.get_event_loop().run_until_complete(self.get_message())

  def set_lock_handler(self, func):
    """Set the handler function for the lock request."""
    global lock_handler
    lock_handler = func

  def set_unlock_handler(self, func):
    """Set the handler function for the unlock request."""
    global unlock_handler
    unlock_handler = func

  def shutdown(self):
    print("Shutting down websocket...")
    self.alive = False
    if self.socket is not None:
      self.socket.close()

  async def get_message(self):
    async with websockets.connect(self.uri) as ws:
      print("Connected!")
      self.socket = ws
      await ws.send(f"Hello!")
      while self.alive:
        msg = await ws.recv()

        if msg.startswith("lock"):
          print("Lock requested:", msg)
          lock_handler()
        elif msg.startswith("unlock"):
          print("Unlock requested:", msg)
          unlock_handler()
        else:
          print("Unknown request!", msg)

