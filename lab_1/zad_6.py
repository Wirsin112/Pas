import socket
from sys import argv


if __name__ == '__main__':

    if len(argv) == 3:
        try:
            socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect_ex((argv[1], int(argv[2])))
        except socket.error as ex:
            print(ex)
            print('1')
    else:
        print("Wrong input.")
