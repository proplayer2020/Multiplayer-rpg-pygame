
import socket
from clientgui import *
import ast


client = None
SIZE = 4096
FORMAT = "utf-8"
connected = False
pseudos = []
def newplayer(username,password,connectiontype):
    global connected,client
    valid = 0
    globalid = 0
    #IP = socket.gethostbyname(socket.gethostname())
    IP = ""
    PORT = 4003
    ADDR = (IP, PORT)
    SIZE = 4096
    FORMAT = "utf-8"
    DISCONNECT_MSG = "!DISCONNECT"
    
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)
    print("connected")
    info = valid_connection(username,password,connectiontype,client)
    if info != "loginvalid":
        return info,client
    else:
        connected = True
        return "quit", client

entities = []
ids = []
idsreceived = []

#width, height = 1200, 800
#screen = pygame.display.set_mode((width, height))


    
    
def valid_connection(usr,pwd,cotype,client,SIZE=1024,FORMAT="utf-8"):
    stop = False
    msg = str(cotype)+","+str(usr)+","+str(pwd)
    print(msg)
    client.send(msg.encode(FORMAT))
    while stop == False:    
        msg = client.recv(SIZE).decode(FORMAT)
        if msg != "":
            if msg == "loginvalid":
                return "loginvalid"
            if msg == "logininvalid":
                return "logininvalid"
            if msg == "registervalid":
                return "registervalid"
            if msg == "registerinvalid":
                return "registerinvalid"
            
        

