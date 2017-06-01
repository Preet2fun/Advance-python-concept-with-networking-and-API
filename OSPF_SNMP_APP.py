###################### OSPF-SNMP APP : Part 1 ####################################

'''
Make below configuration on all router in network for SNMP

configure terminal
snmp-server community public RO
'''

'''
steps for execution of scripts :
1) Open a linux terminal and go to folder containing script.
2) enter 'sudo python OSPF_SNMP_APP.py' and enter root passowrd
3) if file desen't contain execution permission then provide using below command.
    chmod 755 OSPF_SNMP_APP.py
'''
'''
please download required modules as mention below
1) https://pypi.python.org/pypi/networkx/1.11
2) https://pypi.python.org/pypi/matplotlib
3) https://pypi.python.org/pypi/pysnmp
4) https://pypi.python.org/pypi/colorama

'''

import pprint
import subprocess
import binascii
import sys

try:
    #module for output coloring
    from colorama import init, deinit, Fore, Style

except ImportError:
    print Fore.RED + Style.BRIGHT + "\n* Module colorama need to be install on your system"
    print "* download it from above mention link" + Fore.WHITE + Style.BRIGHT
    sys.exit()

try:
    # Module for 2D graph plotting
    import matplotlib.pyplot as matp

except ImportError:
    print Fore.RED + Style.BRIGHT + "\n* Module matplot need to be install on your system"
    print "* download it from above mention link" + Fore.WHITE + Style.BRIGHT
    sys.exit()

try:
    import networkx as nx

except ImportError:
    print Fore.RED + Style.BRIGHT + "\n* Module networkX need to be install on your system"
    print "* download it from above mention link" + Fore.WHITE + Style.BRIGHT
    sys.exit()

try:
    #module for SNMP
    from pysnmp.entity.rfc3413.oneliner import cmdgen

except ImportError:
    print Fore.RED + Style.BRIGHT + "\n* Module snmp need to be install on your system"
    print "* download it from above mention link" + Fore.WHITE + Style.BRIGHT
    sys.exit()

#initialize colorama
init()



#main page of application
#prompt user for input
try:
    print Fore.GREEN + Style.BRIGHT + "##################### OSPF Discovery Tool ##############"
    print "Make sure SNMP community name are same on all Device and its running OSPF!\n"
    ip = raw_input(Fore.BLUE + Style.BRIGHT + "\n* Please enter device IP address : ")
    comm = raw_input("\n* please enter community string name : ")

except KeyboardInterrupt:
    print Fore.RED + Style.BRIGHT + "\n\n* User has aborted program...Exiting \n"
    sys.exit()


###################### OSPF-SNMP APP : Part 1 ####################################

#check IP address validity
def is_ip_valid():
    while True:
        a = ip.split('.')

        if(len(a) == 4) and (1 <= int(a[0]) <= 223) and (int(a[0]) != 127) and (int(a[0]) != 169 or int(a[0]) != 254):
            break
        else:
            print "Invalid IP Address... Please try again.."
            sys.exit()
'''
    # Checking IP reachability
    print Fore.GREEN + Style.BRIGHT + "Checking IP rechability..."

    while True:
        ping_reply = subprocess.call(['ping', '-c', '3', '-w', '3', '-q', '-n', ip], stdout=subprocess.PIPE)

        if ping_reply==0:
            print Fore.GREEN + Style.BRIGHT + "Device is reachable...Now performing SNMP extraction"
            break

        elif(ping_reply==2):
            print  Fore.RED + Style.BRIGHT + "No response from Device {}".format(ip)
            sys.exit()

        else:
            print Fore.RED + Style.BRIGHT + "Ping to following device has failed..."
            print "\n"
            sys.exit()
'''
# Calling IP validity function
try:
    is_ip_valid()

except KeyboardInterrupt:
    print Fore.RED + Style.BRIGHT + "\n\n* User has aborted program...Exiting \n"
    sys.exit()

# define OSPF list
ospf = []

#SNMP function
def snmp_get(ip):
    nbridlist = []
    nbriplist = []
    # define directory to store different parameters and value like host name, neighbour ID and IP
    ospf_devices = {}

    #creating command generator object
    cmdGen = cmdgen.CommandGenerator()

    #Performing SNMP GETNEXT operation on ospf OID

    errorIndication, errorStatus, errorIndex, brTable = cmdGen.nextCmd(cmdgen.CommunityData(comm),cmdgen.UdpTransportTarget((ip,161)),'1.3.6.1.2.1.14.10.1.3')
    #print " Output for first OID : {}".format(cmdGen.nextCmd(cmdgen.CommunityData(comm),cmdgen.UdpTransportTarget((ip,161)),'1.3.6.1.2.1.14.10.1.3'))
    print "brtable value : {}".format(brTable)

    errorIndication, errorStatus, errorIndex, brIpTable = cmdGen.nextCmd(cmdgen.CommunityData(comm), cmdgen.UdpTransportTarget((ip, 161)), '1.3.6.1.2.1.14.10.1.1')
    #print " Output for second OID : {}".format(cmdGen.nextCmd(cmdgen.CommunityData(comm), cmdgen.UdpTransportTarget((ip, 161)), '1.3.6.1.2.1.14.10.1.1'))
    print "brIptable value : {}".format(brIpTable)

    errorIndication, errorStatus, errorIndex, brHostTable = cmdGen.nextCmd(cmdgen.CommunityData(comm),cmdgen.UdpTransportTarget((ip, 161)),'1.3.6.1.4.1.9.2.1.3')
    #print " Output for third OID : {}".format(cmdGen.nextCmd(cmdgen.CommunityData(comm),cmdgen.UdpTransportTarget((ip, 161)),'1.3.6.1.4.1.9.2.1.3'))
    print "brHosttable value : {}".format(brHostTable)

    errorIndication, errorStatus, errorIndex, brHostIdTable = cmdGen.nextCmd(cmdgen.CommunityData(comm),cmdgen.UdpTransportTarget((ip, 161)),'1.3.6.1.2.1.14.1.1')
    #print " Output for fourth OID : {}".format(cmdGen.nextCmd(cmdgen.CommunityData(comm),cmdgen.UdpTransportTarget((ip, 161)),'1.3.6.1.2.1.14.1.1'))
    print "brHostIdtable value : {}".format(brHostIdTable)



    #extract and printout the status
    for brTable_row in brTable:
        for oid, br_id in brTable_row:
            hex_string = binascii.hexlify(str(br_id))
            print hex_string
            octets = [hex_string[i:i+2] for i in range(0,len(hex_string),2)]
            print octets
            ip = [int(i,16) for i in octets]
            print ip
            n_br_id = '.'.join(str(i) for i in ip)
            print n_br_id
            nbridlist.append(n_br_id)
            print ('%s=%s' % (oid,n_br_id))


    for brIpTable_row in brIpTable:
        for oid, br_id in brIpTable_row:
            hex_string = binascii.hexlify(str(br_id))
            print hex_string
            octets = [hex_string[i:i+2] for i in range(0,len(hex_string),2)]
            print octets
            ip = [int(i,16) for i in octets]
            print ip
            n_br_ip = '.'.join(str(i) for i in ip)
            print n_br_ip
            nbriplist.append(n_br_ip)
            print ('%s=%s' % (oid,n_br_ip))


    for brHostTable_row in brHostTable:
        for oid, host in brHostTable_row:
            ospf_host = str(host)
            print ('%s=%s' % (oid, host))


    for brHostIdTable_row in brHostIdTable:
        for oid, hostid in brHostIdTable_row:
            hex_string = binascii.hexlify(str(hostid))
            print hex_string
            octets = [hex_string[i:i+2] for i in range(0,len(hex_string),2)]
            print octets
            ip = [int(i,16) for i in octets]
            print ip
            ospf_host_id = '.'.join(str(i) for i in ip)
            print ospf_host_id
            print ('%s=%s' % (oid, ospf_host_id))


    #  Adding OSPF data by device in  OSPF_device directory
    ospf_devices["Host"]=ospf_host
    ospf_devices["HostId"] = ospf_host_id
    ospf_devices["NbrRtrId"] = nbridlist
    ospf_devices["NbrRtrIp"] = nbriplist

    x = ospf.append(ospf_devices)
    print "Value of X : {}".format(x)
    return ospf

# calling the function for user specific IP address
ospf = snmp_get(ip)
pprint.pprint(ospf)


###################### OSPF-SNMP APP : Part 3 ####################################

def find_unqueried_neighbours():

#host OSPF router IDs
    all_host_ids = []

    for n in range(0, len(ospf)):
        hid = ospf[n]["HostId"]
        all_host_ids.append(hid)

    print "HID"
    print all_host_ids

#neighbour OSPF router ids

    all_nbr_ids = []
    for n in range(0, len(ospf)):
        for each_nid in ospf[n]["NbrRtrId"]:
            if each_nid == '0.0.0.0':
                pass
            else:
                all_nbr_ids.append(each_nid)

    print "NBR"
    print all_nbr_ids


    # determine which neighbour were not queried and adding them to list
    all_outsiders = []
    for p in all_nbr_ids:
        if p not in all_host_ids:
            all_outsiders.append(p)

    print "OUT"
    print all_outsiders

    # run snmp_get function for all unquried neighbour

    for q in all_outsiders:
        for r in range(0,len(ospf)):
            for Index, s in enumerate(ospf[r]["NbrRtrId"]):
                print Index, s
                if q == s:
                    new_IP = ospf[r]["NbrRtrIp"][Index]
                else:
                    pass


    return all_host_ids, all_nbr_ids, ospf

#x = find_unqueried_neighbours()
#pprint.pprint(x)


###################### OSPF-SNMP APP : Part 4 ####################################
# calling above function

while True:

    if (len(list(set(find_unqueried_neighbours()[0])))) == (len(list(set(find_unqueried_neighbours()[1])))):
        break

final_device_list = find_unqueried_neighbours()[2]
pprint.pprint(final_device_list)

#creating list of neighbourship..

neighbourship_dict = {}

for each_directory in final_device_list:
    for index, each_neighbour in enumerate(each_directory["NbrRtrId"]):

        each_tupple = (each_directory["HostId"], each_neighbour)
        neighbourship_dict[each_tupple] = each_directory["NbrRtrIp"][index]

pprint.pprint(neighbourship_dict)


###################### OSPF-SNMP APP : Part 5 ####################################


while True:
    try:
        #user define action
        print Fore.BLUE + Style.BRIGHT + '*Please choose an action : \n\n1 - Display OSPF device on screen\n2- Export OSPF device to CSV file\n3-Generate OSPF network topology'
        user_choice = raw_input("\n* Enter Your Choice : ")
        print "\n"


        #define action
        if user_choice == "1":
            print "pratik"
            for each_dict in final_device_list:
                print "Hostname :" + Fore.YELLOW + Style.BRIGHT + "%s" %each_dict["Host"] + Fore.BLUE + Style.BRIGHT
                print "OSPF RID :" + Fore.YELLOW + Style.BRIGHT + "%s" % each_dict["HostId"] + Fore.BLUE + Style.BRIGHT
                print "OSPF Neighbours by ID :" + Fore.YELLOW + Style.BRIGHT + "%s" % ','.join(each_dict["NbrRtrId"]) + Fore.BLUE + Style.BRIGHT
                print "OSPF Neighbours by IP :" + Fore.YELLOW + Style.BRIGHT + "%s" % ','.join(each_dict["NbrRtrIp"]) + Fore.BLUE + Style.BRIGHT

            continue

        #printing device ti CSV file
        elif user_choice == "2":

            print Fore.CYAN + Style.BRIGHT + "* Generating " + Fore.YELLOW + Style.BRIGHT + "OSPF Device" + Fore.CYAN + Style.BRIGHT + "file....\n"
            print Fore.CYAN + Style.BRIGHT + "Check script folder.import file to EXCEL for better view of device.\n"


            csv_file = open("OSPF_Device.txt", "w")

            print >> csv_file, "Hostname" + ";" + "OSPF RID" + ";" + "OSPF Neighbours by ID" + ";" + "OSPF Neighbours by IP"
            print >> csv_file, each_dict["Host"] + ";" + each_dict["HostId"] + ";" + ','.join(each_dict["NbrRtrId"]) + ";" + ','.join(each_dict["NbrRtrIp"])

            csv_file.close()

            continue

        else:
            print "End of application"

    except KeyboardInterrupt:
        sys.exit()


deinit()


