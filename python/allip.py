#!/usr/bin/python


import os

def get_all_survial_hosts():
    os.system('mkdir -p hosts')
    allips = os.popen('nmap -sn 192.168.1.0/24')
    lines = allips.readlines()
    for line in lines:
        if(line.find("report")>0):
            print line
            host = line.split()
            ip = host[4]
            if not os.path.isfile('hosts/'+ip) :
                os.system('nmap -A ' + ip + ' >> hosts/'+ ip)
        #print line


if __name__ == '__main__':
    get_all_survial_hosts()

