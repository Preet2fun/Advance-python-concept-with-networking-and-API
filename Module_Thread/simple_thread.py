# multitasking using threading module, which is available in python 3.X version and python 2.x version.

from threading import Thread
import time

def print_fun(i):
    print "thread {} started".format(i)
    time.sleep(5)
    print "thread {} stopped".format(i)


for i in range(5):
    t = Thread(target=print_fun, args=(i,))
    t.start()

# multitasking using thread module, which is available in python 2.x version. Now more encouragement for use of threading module instad of thread module
# as it has limited functionality.
import thread
import time

# Define a function for the thread
def print_time( threadName, delay):
   count = 0
   while count < 5:
      time.sleep(delay)
      count += 1
      print "%s: %s" % ( threadName, time.ctime(time.time()) )

# Create two threads as follows
try:
   thread.start_new_thread( print_time, ("Thread-1", 2, ) )
   thread.start_new_thread( print_time, ("Thread-2", 4, ) )
except:
   print "Error: unable to start thread"

while 1:
   pass
"""
Running several threads is similar to running several different programs concurrently, but with the following benefits,

Multiple threads within a process share the same data space with the main thread and can therefore share information or
communicate with each other more easily than if they were separate processes.

Threads sometimes called light-weight processes and they do not require much memory overhead; they are cheaper than processes.

A thread has a beginning, an execution sequence, and a conclusion. It has an instruction pointer that keeps track of
where within its context it is currently running.It can be pre-empted (interrupted)
It can temporarily be put on hold (also known as sleeping) while other threads are running - this is called yielding.


There are two modules which support the usage of threads in Python:
thread and threading

Please note: The thread module has been considered as "deprecated" for quite a long time.
Users have been encouraged to use the threading module instead. So,in Python 3 the module "thread" is not
available anymore. But that's not really true: It has been renamed to "_thread" for backwards incompatibilities in Python3.

The module "thread" treats a thread as a function, while the module "threading" is
implemented in an object oriented way, i.e. every thread corresponds to an object.

"""


