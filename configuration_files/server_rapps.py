import SocketServer
from parser.py import Parser

class AlfaTCPHandler(SocketServer.BaseRequestHandler):
  # Get the parser
  parser = Parser()

  # Handle the AndroidApp request
  def handle(self):
    self.data = self.request.recv(1024).strip()
    # Parse the Json file
    parser.parseJson(data)

# Stablish connections with the AndroidApp
if __name__ == "__main__":
  # TODO define HOST/PORT
  HOST, PORT = "10.0.0.1", 7394
  server = SocketServer.TCPServer((HOST,PORT),AlfaTCPHandler)
  server.serve_forever()
