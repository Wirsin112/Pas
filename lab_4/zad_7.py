import socket
from time import gmtime, strftime

if __name__ == '__main__':
    socketTrue = socket.socket()
    socketTrue.bind(('127.0.0.1', 2905))
    socketTrue.listen(10)
    sock, accept = socketTrue.accept()

    while True:
        if accept:
            data, address = sock.recvfrom(4096)
            print(data)
            data = str(data.decode()).ljust(20)[:20]
            sent = sock.send(data.encode())
            print('[%s] Sent %s bytes bytes back to client %s.' % (
            strftime("%Y-%m-%d %H:%M:%S", gmtime()), sent, address))
