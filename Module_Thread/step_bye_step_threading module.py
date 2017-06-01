import time
import threading

exitflag = 0

class mythread (threading.Thread):
    def __init__(self,threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        print "Staring " + self.name
        display_result(self.name, self.counter,5)
        print "Ending " + self.name

def display_result(thredname, delay, counter):
    while counter:
        if exitflag:
            thredname.exit()
        time.sleep(delay)
        print "%s : %s" %(thredname, time.ctime())
        counter -=1

thread1 = mythread(1, "pratik", 5)
thread2 = mythread(2, "Jay", 5)


thread1.start()
thread2.start()

print "existing main thread"

"""
The newer threading module included with Python 2.4 provides much more powerful, highlevel
support for threads than the thread module discussed in the previous section.

The threading module exposes all the methods of the thread module and provides some
additional methods:

threading.activeCount(): Returns the number of thread objects that are active.
threading.currentThread(): Returns the number of thread objects in the caller's thread control.
threading.enumerate(): Returns a list of all thread objects that are currently active.

In addition to the methods, the threading module has the Thread class that implements
threading. The methods provided by the Thread class are as follows:

run(): The run() method is the entry point for a thread.
start(): The start() method starts a thread by calling the run method.
join([time]): The join() waits for threads to terminate.
isAlive(): The isAlive() method checks whether a thread is still executing.
getName(): The getName() method returns the name of a thread.
setName(): The setName() method sets the name of a thread.

Creating Thread Using Threading Module

To implement a new thread using the threading module, you have to do the following

Define a new subclass of the Thread class.
Override the __init__(self [,args]) method to add additional arguments.
Then, override the run(self [,args]) method to implement what the thread should do
when started.

Once you have created the new Thread subclass, you can create an instance of it and then
start a new thread by invoking the start(), which in turn calls run() method.
"""