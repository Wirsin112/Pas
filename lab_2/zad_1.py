import socket

if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(5)

    try:
        s.connect(('ntp.task.gda.pl', 13))
        print(s.recv(1024))
    except socket.error as exc:
        print("Wyjatek socket.error: " + str(exc))
    s.close()