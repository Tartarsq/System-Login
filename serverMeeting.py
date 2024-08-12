import threading # two things happening at once
import sqlite3
import hashlib
import socket # used to establish the connection between client and server

conn = sqlite3.connect('mydatabase.db', check_same_thread=False)

cursor = conn.cursor()


try:
    ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #We've initialized a TCP server socket using socket.AF_INET and socket.SOCK_STREAM.
    print("[S]: Server socket created")
except socket.error as err:
    print('socket open error: {}\n'.format(err))
    exit()

server_binding = ("localhost", 9999)    
ss.bind(server_binding)
ss.listen()


def start_connection(c): # taking client as parameter
    msg = "Please enter youre username"
    c.send(msg.encode())

    username = c.recv(1024).decode() # 1024 bytes tells us the size / buffer of the content we are recieving so that the socket knows how much to expect
    print("[S]: Data received from client: " + username) 


    

    
    # DO IN GROUPS INDEPENDENTLY
    
    msg2 = "Please enter youre password" 
    c.send(msg2.encode())

    password = c.recv(1024).decode()
    print("[S]: Data received from client: " + password) 

    cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))   
    
    count = cursor.fetchall()
    print(count)

    conn.close()
    if count:
        x = (f"The combination of username '{username}' and password '{password}' exists.")
        c.send(x.encode())

        print("Valid User")
    else:
        x = (f"The combination of username '{username}' and password '{password}' does not exist.")
        c.send(x.encode())
        
        print("Invalid User")


    



while True:
    client, addr = ss.accept()
    t2 = threading.Thread(target=start_connection, args=(client,))
    t2.start()

    # Close the server socket
    ss.close()
    exit()



