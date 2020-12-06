# Author: Campbell Crowley (github@campbellcrowley.com).
import http
import http.server
import threading
import websockets
import asyncio

def undefined_func(self):
  raise Exception('Function not defined!')
begin_registration = undefined_func
verify_code = undefined_func

class WebServer:
  """Doorman Webserver for communicating with client."""

  def __init__(self, port=80, addr='', ws_port=81, ws_host=''):
    """
    Create and start Doorman webserver.

    :param port: Port to listen on.
    :param addr: Address to listen on.
    :return: Nothing.
    """

    print("Starting web server...")
    self.httpd = http.server.ThreadingHTTPServer((addr, port), RequestHandler)
    self.http_thread = threading.Thread(target=self.httpd.serve_forever)
    self.http_thread.start()
    print("Web server running!", port, addr)

    self.sockets = []
    self.socket_server = websockets.serve(self.socket_handler, host=ws_host, port=ws_port)
    self.loop = asyncio.get_event_loop()
    self.socket_thread = threading.Thread(target=self.start_socket_server)
    self.socket_thread.start()

    print("Web sockets listening!", ws_port, ws_host)

  def shutdown(self):
    print("Web server shutting down!")
    self.httpd.shutdown()
    self.http_thread.join()
    self.socket_server.close()

  def set_begin_registration(self, func):
    global begin_registration
    begin_registration = func

  def set_verify_code(self, func):
    global verify_code
    verify_code = func

  def start_socket_server(self):
    asyncio.set_event_loop(self.loop)
    self.loop.run_until_complete(self.socket_server)
    self.loop.run_forever()

  async def socket_handler(self, ws, path):
    print("Socket connected!", path)
    self.sockets.append(ws)

    # await ws.send('lock')
    # await ws.send('unlock')
    try:
      async for message in ws:
        print("WS:", message)
    finally:
      self.sockets.remove(ws)
      print("Socket disconnected.", path)

class RequestHandler(http.server.SimpleHTTPRequestHandler):
  def do_POST(self):
    if not self.path.startswith('/api'):
      self.send_response(404)
      self.end_headers()
      return

    content_length = int(self.headers['Content-Length'])
    post_data = self.rfile.read(content_length)
    post_string = post_data.decode('utf-8')
    print('POST:', post_string)

    if post_string.startswith('verify:'):
      print('Verification request!')
      code = post_string.split(':')[1]
      if verify_code(code):
        print('Verified!')
        self.send_response(201)
      else:
        print('Not verified!')
        self.send_response(403)
      self.end_headers()
    elif post_string.startswith('register'):
      print('Registration request!')

      begin_registration()

      self.send_response(201)
      self.end_headers()
    else:
      self.send_response(400, message="Bad Request")
      self.end_headers()
