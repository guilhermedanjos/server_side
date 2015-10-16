import SocketServer

class AlfaTCPHandler(SocketServer.BaseRequestHandler):
  """
  This class are responsable to handle connection
  Instantiated once per connection to the server
  Override the handle() method to implement communication
  """
  def handle(self):
    self.data = self.request.recv(1024).strip()
    print "{} wrote:".format(self.client_address[0])
    print self.data

if __name__ == "__main__":
  HOST, PORT = "10.42.0.1", 7394

  server = SocketServer.TCPServer((HOST,PORT),AlfaTCPHandler)
  server.serve_forever()

