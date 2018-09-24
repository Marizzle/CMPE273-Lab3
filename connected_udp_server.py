from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor


class ConnectedUDPServer(DatagramProtocol):
    def startProtocol(self):
        host = "127.0.0.1"
        port = 9001 #OVER 9000

        self.transport.connect(host, port)
        print("Server Started")

    def datagramReceived(self, data, addr):

        print("######################################################")
        print("received %r from %s" % (data, addr))
        self.transport.write(b"hello from server")
        print("sent hello to client")
        print("######################################################")

    # Possibly invoked if there is no server listening on the
    # address to which we are sending.
    def connectionRefused(self):
        print("No one listening")

reactor.listenUDP(9000, ConnectedUDPServer())
reactor.run()
