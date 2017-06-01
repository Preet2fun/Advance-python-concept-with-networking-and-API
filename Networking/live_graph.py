import matplotlib.pyplot as plt
import matplotlib.animation as animation
import psutil
from time import gmtime, strftime

print "Start time : {}".format(strftime("%Y-%m-%d %H:%M:%S", gmtime()))

'''
fig=plt.figure()
plt.axis([0,100,0,100])

i=0
x=list()
y=list()

while i <5:
    data = psutil.cpu_percent(interval=5)
    print data
    #x,y = data.split(',')
    x.append(i)
    y.append(data)
    plt.scatter(i,y)
    i+=1
    plt.show()
def animate(i):
    fig = plt.figure()
    ax1 = fig.add_subplot(1,1,1)
    pullData = open("sampleText.txt","r").read()
    dataArray = pullData.split('\n')
    xar = []
    yar = []

    for eachLine in dataArray:
        if len(eachLine)>1:
            x,y = eachLine.split(',')
            xar.append(float(x))
            yar.append(float(y))
    ax1.clear()
    ax1.plot(xar,yar)
    return fig

'''
a=0
myfile = file("sampleText.txt", 'w')
for i in range(0,30):
        a = a + 5
        print >> myfile, "{},{}".format(a, psutil.cpu_percent(interval=1))

myfile.close()


print  "End time : {}".format(strftime("%Y-%m-%d %H:%M:%S", gmtime()))

