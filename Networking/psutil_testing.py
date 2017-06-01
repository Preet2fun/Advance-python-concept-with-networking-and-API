import psutil
print "use cases of psutil.cpu_times"
print psutil.cpu_times()
print psutil.cpu_times(percpu=False)
print psutil.cpu_times(percpu=True)
print "\n"


# 1) CPU SECTION


'''
psutil.cpu_times(percpu=False)[source]
Return system CPU times as a namedtuple. Every attribute represents the seconds the CPU has spent in the given mode. The attributes availability varies depending on the platform:

user: time spent by normal processes executing in user mode; on Linux this also includes guest time
system: time spent by processes executing in kernel mode
idle: time spent doing nothing
Platform-specific fields:

nice (UNIX): time spent by niced processes executing in user mode; on Linux this also includes guest_nice time
iowait (Linux): time spent waiting for I/O to complete
irq (Linux, BSD): time spent for servicing hardware interrupts
softirq (Linux): time spent for servicing software interrupts
steal (Linux 2.6.11+): time spent by other operating systems when running in a virtualized environment
guest (Linux 2.6.24+): time spent running a virtual CPU for guest operating systems under the control of the Linux kernel
guest_nice (Linux 3.2.0+): time spent running a niced guest (virtual CPU for guest operating systems under the control of the Linux kernel)
interrupt (Windows): time spent for servicing hardware interrupts ( similar to irq on UNIX)
dpc (Windows): time spent servicing deferred procedure calls (DPCs); DPCs are interrupts that run at a lower priority than standard interrupts.
When percpu is True return a list of namedtuples for each logical CPU on the system. First element of the list refers to first CPU, second element to second CPU and so on.

'''
print "use cases of psutil.cpu_percent"
print psutil.cpu_percent(interval=1)
print psutil.cpu_percent(interval=None)
print psutil.cpu_percent(interval=1, percpu=True)

for i in range(0,4):
    print psutil.cpu_percent(interval=1)
print "\n"

'''
psutil.cpu_percent(interval=None, percpu=False)[source]
Return a float representing the current system-wide CPU utilization as a percentage.
When interval is > 0.0 compares system CPU times elapsed before and after the interval (blocking).
When interval is 0.0 or None compares system CPU times elapsed since last call or module import, returning immediately.
That means the first time this is called it will return a meaningless 0.0 value which you are supposed to ignore.
In this case is recommended for accuracy that this function be called with at least 0.1 seconds between calls.
When percpu is True returns a list of floats representing the utilization as a percentage for each CPU. First element of
the list refers to first CPU, second element to second CPU and so on. The order of the list is consistent across calls.
'''

print "use cases of psutil.cpu_count"
print psutil.cpu_count()
print psutil.cpu_count(logical=False)
print "\n"


'''
psutil.cpu_count(logical=True)[source]
Return the number of logical CPUs in the system (same as os.cpu_count() in Python 3.4).
If logical is False return the number of physical cores only (hyper thread CPUs are excluded). Return None if undetermined.
'''

print "use cases of psutil.cpu_stats"
#uncomment if you are having Linux OS
#print psutil.cpu_stats()
print "\n"


'''
psutil. cpu_stats()
Return various CPU statistics as a namedtuple:
ctx_switches: number of context switches (voluntary + involuntary) since boot.
interrupts: number of interrupts since boot.
soft_interrupts: number of software interrupts since boot. Always set to 0 on Windows and SunOS.
syscalls: number of system calls since boot. Always set to 0 on Linux.
'''


# 2) MEMORY SECTION

'''
psutil. virtual_memory()
Return statistics about system memory usage as a namedtuple including the following fields, expressed in bytes. Main
metrics:

total: total physical memory.
available: the memory that can be given instantly to processes without the system going into swap. This is
calculated by summing different memory values depending on the platform and it is supposed to be used to
monitor actual memory usage in a cross platform fashion.
Other metrics
used: memory used, calculated differently depending on the platform and designed for informational purposes
only. total - free does not necessarily match used.
free: memory not being used at all (zeroed) that is readily available; note that this doesnot reflect the actual
memory available (use available instead). total - used does not necessarily match free.
active (UNIX): memory currently in use or very recently used, and so it is in RAM.
inactive (UNIX): memory that is marked as not used.
buffers (Linux, BSD): cache for things like file system metadata.
cached (Linux, BSD): cache for various things.
shared (Linux, BSD): memory that may be simultaneously accessed by multiple processes.
wired (BSD, OSX): memory that is marked to always stay in RAM. It is never moved to disk.
The sum of used and available does not necessarily equal total. On Windows available and free are the same. See
meminfo.py script providing an example on how to convert bytes in a human readable form.

Note: if you just want to know how much physical memory is left in a cross platform fashion simply rely on the
available field.

'''

print "use cases of psutil.virual_memory"
print psutil.virtual_memory()
print "\n"

'''
psutil. swap_memory()
Return system swap memory statistics as a namedtuple including the following fields
total: total swap memory in bytes
used: used swap memory in bytes
free: free swap memory in bytes
percent: the percentage usage calculated as (total minus available) / total * 100
sin: the number of bytes the system has swapped in from disk (cumulative)
sout: the number of bytes the system has swapped out from disk (cumulative)
sin and sout on Windows are always set to 0. See meminfo.py script providing an example on how to convert bytes in
a human readable form.
'''

print "use cases of psutil.swap_memory"
print psutil.swap_memory()
print "\n"

# 3) DISK SECTION

'''
psutil. disk_partitions(all=False)
Return all mounted disk partitions as a list of namedtuples including device, mount point and filesystem type, similarly
to df command on UNIX. If all parameter is False it tries to distinguish and return physical devices only e.g. (hard
disks, cdrom drives, USB keys) and ignore all others (e.g. memory partitions such as /dev/shm). Note that this may not
be fully reliable on all systems (e.g. on BSD this parameter is ignored). Namedtuples fstype field is a string which
varies depending on the platform. On Linux it can be one of the values found in /proc/filesystems (e.g. 'ext3' for an ext3
hard drive o 'iso9660' for the CD-ROM drive). On Windows it is determined via GetDriveType and can be either "removable",
"fixed", "remote", "cdrom", "unmounted" or "ramdisk". On OSX and BSD it is retrieved via getfsstat(2). See disk_usage.py script
providing an example usage.
'''

print "use cases of psutil.disk_partitions"
print psutil.disk_partitions()
print "\n"