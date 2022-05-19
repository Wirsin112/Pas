import socket
from time import gmtime, strftime
import datetime

if __name__ == '__main__':
    socketTrue = socket.socket()
    socketTrue.bind(('127.0.0.1', 2917))
    socketTrue.listen(10)
    socketTrue, accept = socketTrue.accept()
    while True:
        if accept:
            data, address = socketTrue.recvfrom(4096)
            print(data)
            time_now = datetime.datetime.utcnow()
            sent = socketTrue.send(str(time_now).encode('utf-8'))
            print('[%s] Sent %s bytes bytes back to client %s.' % (
            strftime("%Y-%m-%d %H:%M:%S", gmtime()), sent, address))
