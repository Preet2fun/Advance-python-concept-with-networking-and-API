import socket
host = "127.0.0.1"
port = 12345
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
try:
    s.bind((host,port))
    #s.settimeout(5)
    s.listen(2)
    while True:
        conn, addr = s.accept()
        print addr, "Now Connected"
        conn.send("Thanks for connecting")

except:
    print ("Server is not connected or down")
    conn.close()