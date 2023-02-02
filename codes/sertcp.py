from socket import *
serverName='DESKTOP-87Q798G'
serverPort = 12530
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind((serverName,serverPort))
serverSocket.listen(1)
print ("The server is ready to receive")
while 1:
    connectionSocket, addr = serverSocket.accept()
    sentence = connectionSocket.recv(2048).decode()
    file=open(sentence,"r")
    l=file.read(2048)
    connectionSocket.send(l.encode())
    file.close()
    connectionSocket.close()
