import socket
from time import gmtime, strftime

if __name__ == '__main__':

    socketTrue = socket.socket()
    socketTrue.bind(('127.0.0.1', 2916))
    socketTrue.listen(10)
    socketTrue, accept = socketTrue.accept()
    while True:
        if accept:
            data, address = socketTrue.recvfrom(4096)
            sent = socketTrue.send(data)
            print('[%s] Sent %s bytes bytes back to client %s.' % (strftime("%Y-%m-%d %H:%M:%S", gmtime()), sent, address))
