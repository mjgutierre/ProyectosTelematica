import socket 

HEADERSIZE = 10

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1024))

while True:
    complete_info = ''
    new_msg = True
    while True:
        msg=s.recv(16)
        if new_msg:
            print(f"new message length: {msg[HEADERSIZE]}") 
            msglen = int(msg[:HEADERSIZE])
            new_msg = False
        
        complete_info += msg.decode("utf-8")

        if len(complete_info)-HEADERSIZE == msglen:
            print("full msg recvd")
            print(complete_info[HEADERSIZE:])
            new_msg = True
            complete_info = ''

    print(complete_info)
