import socket
if __name__ == '__main__':
    a = input("Type file name:\n")
    try:
        socket.inet_aton(a)
        print("git")
    except socket.error:
        print("error")
