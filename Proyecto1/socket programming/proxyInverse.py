# Import required modules
import socket
import sys #options and arguments while running
from _thread import *
from decouple import config

try:
    listening_port= int(input("Enter a listening port: "))
except KeyboardInterrupt:
        print ("\n[*] User has requested an interrupt")
        print ("[*]Application Exiting....")
        sys.exit()

#variables 
max_connection = 5
buffer_size= 8192
#ttl hay que ponerlo

def start(): 
    rr=0
    try: 
        #creates a socket that will act as our server and uses addresses that follow the IPv4 format.
        sock= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('', listening_port))
        sock.listen(max_connection)
        print("Inicializating Socket... Done")
        print("Socket bind succesfully ")
        print ('[*] Server started successfully [{}]'.format(listening_port))
    except Exception:
            print ("[*]Unable to initialize socket" )
            print (Exception)
            sys.exit(2)

    while True:
        try: 
        #grabs a connection from a client, and does something with it. 
            conn, addr = sock.accept() # Establish connection with client.
            data = conn.recv(buffer_size)
            print(data)
            
        #Round robin implementation
            if rr>=len(data):
                    rr=0
            webserver = data[rr]
            rr+=1
            start_new_thread (conn_string,(conn,data,addr))
        
        except KeyboardInterrupt:
            sock.close()
            print("\n[*] Graceful shutdown")
            sys.exit(1)

#implementation of the direction connected to our server
def conn_string (conn, data, addr):
    try: 
        print (data)
        first_line = data.split(b'\n')[0]

        url = first_line.split(" ")[1]
        http_pos = url.find(b'://')
        if(http_pos==-1):
            temp=url
        else:
            temp= url[(http_pos+3):]

        port_pos = temp.find(b':')

        webserver_pos = temp.find(b'/')

        if webserver_pos == -1:
            webserver_pos =len(temp)
            webserver = ""
            port = -1 

        if (port_pos == -1 or webserver_pos < port_pos):
            port= 8080
            webserver = temp[:webserver_pos]
        else: 
            port = int((temp[(port_pos+1):])[:webserver_pos-port_pos-1])
            webserver = temp[port_pos]
        
        print(webserver)
        print("va a entrar al proxy")
        proxy_server(webserver, port, conn, addr, data)
    except Exception:
        pass

#proxy server implementation
def proxy_server(webserver, port, conn, addr, data):
    print("esta entrando al proxy server")
    try: 
        #print(data)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((webserver,port))
        print("se conecto el server" )#,webserver
        sock.sendall(data)#lo cambie por sendall peroestaba en send
        print("se envio algo")

        while True:
            reply = sock.recv(buffer_size)
          
            if len(reply) > 0: 
                    conn.send(reply)

                    dar=float(len(reply))
                    dar= float (dar/1024)
                    dar= "{}.3s".format(dar)
                    dar='%s KB' % (dar)
                    print('[*] Request Done: {} => {} <= {}'.format(addr[0],dar, webserver))
                    print(reply)
            else: 
                break

        sock.close()

        conn.close()
    except socket.error:
        sock.close() 
       # Clean up the connection
        conn.close()
        print(sock.error)
        sys.exit(1)

if __name__ == '__main__':
    start()