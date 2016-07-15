__author__ = 'Wenyu'

from BaseHTTPServer import HTTPServer
from SocketServer import ThreadingMixIn
import threading


class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
  def shutdown(self):
    self.socket.close()
    HTTPServer.shutdown(self)


class SimpleHttpServer():
  def __init__(self, address, port, handler):
    self.server = ThreadedHTTPServer((address,port), handler)

  def start(self):
    self.server_thread = threading.Thread(target=self.server.serve_forever)
    self.server_thread.daemon = True
    self.server_thread.start()

  def waitForThread(self):
    self.server_thread.join()

  def stop(self):
    self.server.shutdown()
    self.waitForThread()