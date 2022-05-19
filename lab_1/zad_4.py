from sys import argv
import socket
if __name__ == '__main__':
    if len(argv) == 2:
        try:
            socket.inet_aton(argv[1])
            a = socket.gethostbyaddr(argv[1])
            print(a)
        except socket.error:
            print("error")
