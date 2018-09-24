from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor


class ConnectedUDPClient(DatagramProtocol):
    def startProtocol(self):
        host = "127.0.0.1"
        port = 9000

        self.transport.connect(host, port)
        print("Connected to server @ {} {}".format(host, port))
        self.transport.write(b"hello from client")  # no need for address
        print("Sent Data to Server")

    def datagramReceived(self, data, addr):
        print("######################################################")
        print("received %r from %s" % (data, addr))
        print("######################################################")

    # Possibly invoked if there is no server listening on the
    # address to which we are sending.
    def connectionRefused(self):
        print("No one listening")

reactor.listenUDP(9001, ConnectedUDPClient())
reactor.run()
