from socket import *

serverIP = "127.0.0.1"
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)

text = input("Enter file name: ")
clientSocket.sendto(bytes(text, "utf-8"), (serverIP, serverPort))
filecontents, serverAddr = clientSocket.recvfrom(2048)
print("From Server: ", filecontents.decode())
clientSocket.close()
