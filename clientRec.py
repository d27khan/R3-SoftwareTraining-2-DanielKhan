import socket

buffersize = 64
while 1:

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((socket.gethostname(), 1235))
    s.listen(1)

    clientsocket,address = s.accept()

    pos = clientsocket.recv(buffersize)
    clientsocket.send(pos)

clientsocket.close()