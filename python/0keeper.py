#!/usr/bin/python

import sys
import http.client
import requests
import json

recorder_file='0keeper.md'

def mac_isexist(mac):
    f1=file(recorder_file)
    #print("we are find " + mac)
    for line in f1.readlines():
        #print line
        if(line.find(mac)>0):
            print(mac+" is add before")
            return True
    return False

def addit(cname, mac, ip):
    if(mac_isexist(mac)):
        return False
    f1=file(recorder_file, 'a')
    for _ in range(55-len(cname)):
        cname += " "
    print(mac+"will add")
    f1.write(cname + ' | ' +mac + ' | '+ ip + '\n')
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
