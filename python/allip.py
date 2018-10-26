#!/usr/bin/python


import os
import sys

def get_all_survial_hosts(ips):
    os.system('mkdir -p hosts')
    #allips = os.popen('nmap -sn 192.168.1.0/24')
    allips = os.popen('nmap -sn ' + ips)
    lines = allips.readlines()
    for line in lines:
        if(line.find("report")>0):
            #print line
            host = line.split()
            ip = host[len(host)-1]
            ip = ip.replace('(', '')
            ip = ip.replace(')', '')
            #print ip
            if not os.path.isfile('hosts/'+ip) :
                print 'checking ' +ip + '.....'
                os.system('nmap -A ' + ip + ' >> hosts/'+ ip)
            else:
                print 'we have checked ' + ip 
        #print line


if __name__ == '__main__':
    if len(sys.argv) == 1 :
        get_all_survial_hosts('192.168.1.0/24')
    else:
        get_all_survial_hosts(sys.argv[1])

