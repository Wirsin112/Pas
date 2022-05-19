import socket

if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(5)
    try:
        s.connect(('212.182.24.27', 2900))
        a = "Test"
        s.send(a.encode())
        print(s.recv(1024))
    except socket.error as exc:
        print("Exception socket.error: " + str(exc))
    s.close()
