import threading
import socket

try:
    cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # AF_INET --> types of address your program can work with
    print("[C]: Client socket created")
except socket.error as err:
    print('socket open error: {} \n'.format(err))
    exit()

# connect to the server on local machine
server_binding = ("localhost", 9999)
cs.connect(server_binding)

# recieve data from server: Welcome to Blueprint  
data_from_server=cs.recv(1024)
message = data_from_server.decode()
print("[C]: Data received from server: " + message)    
cs.send(input("Response here: ").encode())

# IN GROUPS

# receive data from server: How are you
data_from_server=cs.recv(1024)
message = data_from_server.decode()
print("[C]: Data received from server: " + message)    
cs.send(input("Response here: ").encode())


data_from_server=cs.recv(1024)
message = data_from_server.decode()
print("[C]: Data received from server: " + message) 



# close the client sockets
cs.close()
exit()