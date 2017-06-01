import socket
'''
a = socket.gethostbyname("www.google.com")
f = socket.gethostbyaddr("216.58.197.68")
print a
print f
b = socket.gethostbyname_ex("cisco.com")
print b
c = socket.gethostname()
print c

d = socket.gethostbyname_ex(socket.gethostname())
print d

e = socket.getfqdn("facebook.com")
print e

print socket.getservbyname("http")
print socket.getservbyname("smtp")
'''
rmip = "127.0.0.1"
port_list = [25,80,441,22,23,912,135,20]
for port in port_list:
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    result = s.connect_ex((rmip,port))
    print port, ":" ,result
    s.close()

