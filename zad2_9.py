import socket


def recv_all(socketAll, crlf):
    dataAll = ""
    while not dataAll.endswith(crlf):
        dataAll = dataAll + socketAll.recv(1)
    return dataAll


def recv_until(socketUnit, size):
    dataUnit = ""
    i = 0
    while i < size:
        dataUnit = dataUnit + socketUnit.recv(1)
        i = i + 1
    return dataUnit


if __name__ == '__main__':
    socketTrue = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socketTrue.connect(("httpbin.org", 80))

    request = 'GET /image/png HTTP/1.1\r\nHost: httpbin.org\r\nUser-Agent: Mozilla/4.0 (compatible; MSIE 5.5; AOL 4.0; Windows 98)\r\n\r\n'

    socketTrue.sendall(request)

    response = recv_all(socketTrue, "\r\n\r\n")
    headers = response

    headers = response.split('\r\n')

    for header in headers:
        if "Content-Length:" in header:
            size = int(header.split(" ")[-1])

    data = recv_until(socketTrue, size)

    file = open("image.png", "w")

    file.write(data)
    file.close()
