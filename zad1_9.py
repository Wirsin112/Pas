import socket


def recv_all(socketFun, crlf):
    data = ""
    while not data.endswith(crlf):
        data = data + socketFun.recv(1)
    return data


def recv_until(sock, size):
    data = ""
    i = 0
    while i < size:
        data = data + sock.recv(1)
        i = i + 1
    return data


if __name__ == '__main__':
    socketTrue = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socketTrue.connect(("httpbin.org", 80))

    request = 'GET /html HTTP/1.1\r\nHost: httpbin.org\r\nUser-Agent: Mozilla/4.0 (compatible; MSIE 5.5; AOL 4.0; Windows 98)\r\n\r\n'

    socketTrue.sendall(request)

    headers = recv_all(socketTrue, "\r\n\r\n").split('\r\n')

    for header in headers:
        if "Content-Length:" in header:
            size = int(header.split(" ")[-1])

    data = recv_until(socketTrue, size)

    file = open("page.html", "w")

    file.write(data)
    file.close()
