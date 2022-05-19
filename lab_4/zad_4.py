import socket
from time import gmtime, strftime
import datetime

if __name__ == '__main__':
    socketTrue = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    socketTrue.bind(('127.0.0.1', 2917))
    while True:
        data, address = socketTrue.recvfrom(4096)
        result = eval(data.decode('utf-8'))
        time_now = datetime.datetime.utcnow()
        sent = socketTrue.sendto(str(result).encode("utf-8"), address)
        print('[%s] Sent %s bytes bytes back to client %s.' % (strftime("%Y-%m-%d %H:%M:%S", gmtime()), sent, address))