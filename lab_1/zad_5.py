from sys import argv
import socket
if __name__ == '__main__':
    if len(argv) == 2:
        a = socket.gethostbyname(argv[1])
        print(a)

