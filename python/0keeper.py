#!/usr/bin/python

import sys
import http.client
import requests
import json
import datetime
import time
import os

recorder_file='0keeper.md'
log_file='0keeper.log'

def cur_file_dir():
     path = sys.path[0]
     if os.path.isdir(path):
         return path + '/'
     elif os.path.isfile(path):
         return os.path.dirname(path)

def mac_isexist(cname, mac, ip, lease_time):
    f1=file(cur_file_dir() + recorder_file)
    #print("we are find " + mac)
    lines = f1.readlines()
    foundit = False
    f1=file(cur_file_dir() + recorder_file, 'w')
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
    f1=file(cur_file_dir() + recorder_file, 'r')
    content=f1.readline()
    content+=f1.readline()
    print(mac+" " + ip + "  " +cname + lease_time + " is new user.")
    content+=cname + ' | ' +mac + ' | '+ ip + '  | ' + lease_time + '\n'
    content+=f1.read()
    f1.close
    f1=file(cur_file_dir() +recorder_file,'w')
    f1.write(content)
    f1.close
    return True

def addlog(content2):
    f1=file(cur_file_dir() + log_file, 'r')
    readlines = f1.read()
    #print readlines
    if(readlines.find(content2)>=0):
        return
    readlines +=  content2 + '\n'
    f1=file(cur_file_dir() + log_file, 'w')
    f1.write(readlines)
    return

def addhttp1():
   connection = http.client.HTTPConnection('192.168.19.1', 80, timeout=10) 
   connection.request("GET", "/")
   response = connection.getresponse()
   print(response.read())
   connection.close()

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
        datetime_struct = datetime.datetime.fromtimestamp(float(time1)-60*60*24)
        localtime=datetime_struct.strftime(" %Y-%m-%d %H:%M:%S")
        if(addit(pcname, mac, ip, localtime)):
            count += 1
        #print(mac, ip, pcname,time1)
        #print time.localtime(float(time1))
        #print localtime
    print "add ", count 
    os.system("cat 0keeper.md | grep ':' | sort -r -k 6 -o 0keeper.md")

if __name__ == '__main__':
    if(len(sys.argv) == 1):
        addhttp()
    else:
	    addit(sys.argv[1], sys.argv[2], sys.argv[3],sys.argv[4])
