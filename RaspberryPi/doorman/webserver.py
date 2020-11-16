import http
import http.server
import threading

class WebServer:
  """Doorman Webserver for communicating with client."""

  def __init__(self, port=80, addr=''):
    """
    Create and start Doorman webserver.

    :param port: Port to listen on.
    :param addr: Address to listen on.
    :return: Nothing.
    """

    print("Starting web server...")
    self.httpd = http.server.ThreadingHTTPServer((addr, port), RequestHandler)
    self.thread = threading.Thread(target=self.httpd.serve_forever)
    self.thread.start()
    print("Web server running!")

  def shutdown(self):
    print("Web server shutting down!")
    self.httpd.shutdown()
    self.thread.join()

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

    if post_string.startswith('verify'):
      print('Verification request!')
      self.send_response(201)
      self.end_headers()
    elif post_string.startswith('register'):
      print('Registration request!')
      self.send_response(201)
      self.end_headers()
    else:
      self.send_response(400, message="Bad Request")
      self.end_headers()
