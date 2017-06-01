import os
response = os.popen('ping -n 1 192.168.20.155')
for line in response.readlines():
    print line,