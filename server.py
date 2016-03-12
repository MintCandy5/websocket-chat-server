import signal, sys, ssl
from SimpleWebSocketServer import WebSocket, SimpleWebSocketServer, SimpleSSLWebSocketServer
from optparse import OptionParser

clients = []
i = 0
class SimpleChat(WebSocket):

    def handleMessage(self):
      print self.data

    def handleConnected(self):
       print self.address, 'connected'
       clients.append(self)

    def handleClose(self):
       clients.remove(self)
       print self.address, 'closed'

server = SimpleWebSocketServer('', 8000, SimpleChat)
server.serveforever()
