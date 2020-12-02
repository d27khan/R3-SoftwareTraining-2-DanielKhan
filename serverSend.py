import socket
import datetime

buffersize = 256
#sending the position of the motor and which dir to travel in
def sendPos(pathArr):
    

   # adjusting the array to provide the string for the arduino motor
    if pathArr == "N":
        pathArr = "[255][0][255][0]"
    if pathArr== "S":
        pathArr= "[0][255][0][255]"
    if pathArr== "E":
        pathArr = "[255][0][][255]"
    if pathArr == "W":
        pathArr = "[0][255][255][0]"

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((socket.gethostname(), 1235))
    s.send(pathArr.encode('utf-8'))
    pos = s.recv(buffersize)
    s.close

    print(pos)


    








