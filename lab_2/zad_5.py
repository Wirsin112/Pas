import socket

if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(5)
    exit_program = False
    try:
        s.connect(('212.182.24.27', 2901))
    except socket.error as exc:
        print("Exception socket.error: " + str(exc))
        exit_program = True

    if exit_program:
        while True:
            a = input("Input message:\n")
            s.send(a.encode())
            print(s.recv(1024))
    s.close()
