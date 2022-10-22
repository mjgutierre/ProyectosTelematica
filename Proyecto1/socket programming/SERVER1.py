import socket

HEADERSIZE = 10

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1024))
s.listen(5) #queue of 5 
while True:
    clientsocket, address=s.accept()
    print(f"Connection to {address} established")
    msg = "Server"
    msg = (f'{len(msg):<{HEADERSIZE}}'+msg)# 

    clientsocket.send(bytes(msg, "utf-8"))#send inf to the client socket
