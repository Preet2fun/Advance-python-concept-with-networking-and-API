import threading
import time
import psutil
from matplotlib import pyplot as plt
from matplotlib import animation


class mythread (threading.Thread):
    def __init__(self,fun_ID):
        threading.Thread.__init__(self)
        self.fun_ID = fun_ID
        #self.name = name
        #self.counter = counter

    def run(self):
        print 2
        if self.fun_ID == 1:
            writing()
        elif self.fun_ID == 2:
            animate()


def writing():
    print 3
    myfile = file("sampleText.txt", 'w')
    for i in range(0,10):
        i = i + 1
        print >> myfile, "{},{}".format(i, psutil.cpu_percent(interval=2))
    myfile.close()

# Define a function for the thread
def animate(i):
    print 4
    pullData = open("sampleText.txt","r").read()
    dataArray = pullData.split('\n')
    xar = []
    yar = []

    for eachLine in dataArray:
        if len(eachLine)>1:
            x,y = eachLine.split(',')
            xar.append(float(x))
            yar.append(float(y))

    line.set_data(xar, yar)
    return line,

# First set up the figure, the axis, and the plot element we want to animate
print 1
# Create two threads as follows
try:
   thread1 = mythread(1)
   thread2 = mythread(2)

except:
   print "Error: unable to start thread"

thread1.start()
thread2.start()

fig = plt.figure()
ax = plt.axes(xlim=(0, 150), ylim=(0, 30))
line, = ax.plot([], [], lw=2)

def init():
    line.set_data([], [])
    return line,

anim = animation.FuncAnimation(fig, animate, init_func=init, frames=50, interval=1, blit=True)
plt.show()

print "end"