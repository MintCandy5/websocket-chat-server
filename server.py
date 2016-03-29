import signal, sys, ssl
from SimpleWebSocketServer import WebSocket, SimpleWebSocketServer, SimpleSSLWebSocketServer
from optparse import OptionParser

clients = []
class SimpleChat(WebSocket):

    def handleMessage(self):
        words = self.data.split('\xfe')
        print("\nCount={0}".format(len(words)))
        for w in words:
            print ''.join(' {:02x}'.format(x) for x in w)

    def handleConnected(self):
       print self.address, 'connected'
       for client in clients:
          client.sendMessage(self.address[0] + u' - connected')
       clients.append(self)

    def handleClose(self):
       clients.remove(self)
       print self.address, 'closed'
       for client in clients:
          client.sendMessage(self.address[0] + u' - disconnected')

server = SimpleWebSocketServer('', 8000, SimpleChat)
server.serveforever()
