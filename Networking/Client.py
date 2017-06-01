import socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = "127.0.0.1"
port = 12345
s.connect((host,port))
buf = bytearray("-" * 30)
print "Number of Bytes :", s.recv_into(buf)
print buf
t = s.recv(1024)
print t
s.send("Hello Server!!!")
s.close()
