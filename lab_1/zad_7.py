import socket
from sys import argv


if __name__ == '__main__':
    works = []
    if len(argv) == 2:
        for i in range(10000):
            print(str(i)+"/10_000")
            try:
                socket.setdefaulttimeout(0.001)
                socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((argv[1], i))
                works.append(i)
            except socket.error as ex:
                pass
        for i in works:
            print(str(i), "Open")
        if len(works) == 0:
            print("Didn't found open port.")
    else:
        print("Wrong input.")