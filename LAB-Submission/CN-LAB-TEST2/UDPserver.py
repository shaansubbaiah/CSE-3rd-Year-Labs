from socket import *

serverIP = "127.0.0.1"
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)

serverSocket.bind((serverIP, serverPort))
print("The server is ready to receive")

while 1:
    sentence, clientAddr = serverSocket.recvfrom(2048)

    file = open(sentence, "r")
    text = file.read(2048)

    serverSocket.sendto(bytes(text, "utf-8"), clientAddr)
    print("Sent back to client: ", text)
    file.close()
