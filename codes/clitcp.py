from socket import *
serverName = 'DESKTOP-87Q798G'
serverPort = 12530
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
sentence = input("Enter file name: ")
clientSocket.send(sentence.encode())
filecontents = clientSocket.recv(2048).decode()
print ('From Server:', filecontents)
clientSocket.close()
