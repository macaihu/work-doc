#!/usr/bin/python3

import sys
import http.client
import requests
import json
import datetime
import time
import os

#wget http://standards-oui.ieee.org/oui/oui.csv -O oui.csv
recorder_file='0keeper.md'
log_file='0keeper.log'

def cur_file_dir():
     path = sys.path[0]
     if os.path.isdir(path):
         return path + '/'
     elif os.path.isfile(path):
         return os.path.dirname(path)

def mac_isexist(cname, mac, ip, lease_time):
    f1=open(cur_file_dir() + recorder_file)
    #print("we are find " + mac)
    lines = f1.readlines()
    foundit = False
    f1=open(cur_file_dir() + recorder_file, 'w')
    for line in lines:
        #print line
        if(line.find(mac)>0):
            print(mac+" " + ip + "  " +cname + lease_time + " come again.")
            foundit = True
            line = cname + ' | ' +mac + ' | '+ ip + '  | ' + lease_time + '\n'
        f1.write(line)
    return foundit

def addit(cname, mac, ip, lease_time):
    for _ in range(32-len(cname)):
        cname += " "    
    for _ in range(14-len(ip)):
        ip += " "    
    addlog(cname + ' | ' +mac + ' | '+ ip + '  | ' + lease_time )
    if(mac_isexist(cname, mac, ip, lease_time)):
        return False
    f1=open(cur_file_dir() + recorder_file, 'r')
    content=f1.readline()
    content+=f1.readline()
    print(mac+" " + ip + "  " +cname + lease_time + " is new user.")
    content+=cname + ' | ' +mac + ' | '+ ip + '  | ' + lease_time + '\n'
    content+=f1.read()
    f1.close
    f1=open(cur_file_dir() +recorder_file,'w')
    f1.write(content)
    f1.close
    return True

def addlog(content2):
    f1=open(cur_file_dir() + log_file, 'r')
    readlines = f1.read()
    #print readlines
    if(readlines.find(content2)>=0):
        return
    readlines +=  content2 + '\n'
    f1=open(cur_file_dir() + log_file, 'w')
    f1.write(readlines)
    return

def addhttp1():
   connection = http.client.HTTPConnection('192.168.19.1', 80, timeout=10) 
   connection.request("GET", "/")
   response = connection.getresponse()
   print(response.read())
   connection.close()

def find_oui(mac):
    shortmac=mac.replace(':', '')[:6]
    #print '1111111111111111111 '+shortmac
    oui = os.popen("cat oui.csv | grep " + shortmac).readline()
    #print oui
    company = oui.split(',')[2][0:31]       
    if company[0] == '\"':
        company = oui.split(',')[2][1:32]       
    company = company.replace(' ', '_')
    #print company
    return company


def addhttp():
    loginpayload={'cmd':100,'method':"POST", 'language':'EN', 'username':'admin', 'passwd':'f6339c4179e7b9b4b7c9da08502184ec', 'sessionId':'a6083050f134e86e79a7af2a5217ab4ea0ff26b8b1a25ea4b45fb969aa49d457' }
    test = 'test=test'
    headers = {'Content-Type' : 'multipart/form-data'}
    login = requests.post('http://192.168.19.1/cgi-bin/http.cgi', params=loginpayload, headers=headers, data=test)
    #print(login.status_code)
    #print(login.text)
    json1={"cmd":122,"method":"GET","language":"CN","sessionId":"a6083050f134e86e79a7af2a5217ab4ea0ff26b8b1a25ea4b45fb969aa49d457"}
    r = requests.post('http://192.168.19.1/cgi-bin/http.cgi', json=json1)
    #print(r.status_code)
    #print(r.json())
    macs=r.json()['data']
    count=0
    for pc in macs:
        time1=pc[0]
        mac=pc[1].upper()
        ip=pc[2]
        pcname=pc[3]
        if pcname == '*':
            pcname = find_oui(mac)
        datetime_struct = datetime.datetime.fromtimestamp(float(time1)-60*60*24)
        localtime=datetime_struct.strftime(" %Y-%m-%d %H:%M:%S")
        if(addit(pcname, mac, ip, localtime)):
            count += 1
        #print(mac, ip, pcname,time1)
        #print time.localtime(float(time1))
        #print localtime
    print("add ", count )
    os.system("cat 0keeper.md | grep ':' | sort -r -k 6 -o 0keeper.md")

if __name__ == '__main__':
    if(len(sys.argv) == 1):
        addhttp()
    elif (sys.argv[1] == 'oui'):
        os.system("wget http://standards-oui.ieee.org/oui/oui.csv -O oui.csv")
    else:
	    addit(sys.argv[1], sys.argv[2], sys.argv[3],sys.argv[4])
