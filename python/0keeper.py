#!/usr/bin/python

import sys
import http.client
import requests
import json
import datetime

recorder_file='0keeper.md'

def mac_isexist(cname, mac, ip):
    f1=file(recorder_file)
    #print("we are find " + mac)
    lines = f1.readlines()
    foundit = False
    f1=file(recorder_file, 'w')
    for line in lines:
        #print line
        if(line.find(mac)>0):
            print(mac+"  "+cname + " come again.")
            foundit = True
            line = cname + ' | ' +mac + ' | '+ ip + '  | ' + datetime.datetime.now().strftime(' %Y-%m-%d')+ '\n'
        f1.write(line)
    return foundit

def addit(cname, mac, ip):
    for _ in range(40-len(cname)):
        cname += " "    
    for _ in range(14-len(ip)):
        ip += " "    
    if(mac_isexist(cname, mac, ip)):
        return False
    f1=file(recorder_file, 'r')
    content=f1.readline()
    content+=f1.readline()
    print(mac+"  "+cname + " is new user.")
    content+=cname + ' | ' +mac + ' | '+ ip + '  | ' + datetime.datetime.now().strftime(' %Y-%m-%d') + '\n'
    content+=f1.read()
    f1.close
    f1=file(recorder_file,'w')
    f1.write(content)
    f1.close
    return True

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
        mac=pc[1].upper()
        ip=pc[2]
        pcname=pc[3]
        if(addit(pcname, mac, ip)):
            count += 1
        #print(mac, ip, pcname)
    print "add ", count 

if __name__ == '__main__':
    if(len(sys.argv) == 1):
        addhttp()
    else:
	    addit(sys.argv[1], sys.argv[2], sys.argv[3])
