import socket

# create a socket object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
host = 'localhost'

port = 12355

# bind the socket to a public host, and a well-known port
serversocket.bind((host, port))

# become a server socket
serversocket.listen(5)

while True:
    # establish a connection
    clientsocket, addr = serversocket.accept()

    print("Got a connection from %s" % str(addr))
    
    # send a thank you message to the client.
    message = "Thank you for connecting" + "\r\n"
    clientsocket.send(message.encode('ascii'))
    while(1):
        message = input()
        clientsocket.send(message.encode('ascii'))
        msg=clientsocket.recv(1024).decode()
        if len(msg)>0:
            
            print(msg)
        if msg=="close" or message=="close":break
    clientsocket.close()