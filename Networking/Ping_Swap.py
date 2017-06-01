import os
import socket
import platform
from datetime import datetime

net = raw_input("Enter the network address for scan :")
net_1 = net.split('.')
a = '.'
net2 = net_1[0]+a+net_1[1]+a+net_1[2]+a
star_add_range = int(raw_input("Enter starting number : "))
end_add_range = int(raw_input("Enter starting number : "))

end_add_range = end_add_range + 1
oper = platform.system()
t1 = datetime.now()
print "Scanning in Progress"
for ip in xrange(star_add_range,end_add_range):
    addr = net2 + str(ip)
    comm = "ping -n 1 " + addr
    print comm
    response = os.popen(comm)
    for line in response.readlines():
        if(line.count("TTL")):
            break
    if(line.count("TTL")):
        print addr, "--> Live"
t2= datetime.now()
total =t2-t1
print "scanning complete in " , total
