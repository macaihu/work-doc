#!/usr/bin/python

import sys
import http.client
import requests
import json

recorder_file='0keeper.txt'


def mac_isexist(mac):
    f1=file(recorder_file)
    for line in f1.readlines():
        if(line.find(mac)):
            print(mac+" is add before")
            return True
    return False

def addit(cname, mac, ip):
    if(mac_isexist(mac)):
        return
    f1=file(recorder_file, 'r+')
    f1.write(cname + ' | ' +mac + ' | '+ ip)
    f1.close

def addhttp1():
   connection = http.client.HTTPConnection('192.168.19.1', 80, timeout=10) 
   connection.request("GET", "/")
   response = connection.getresponse()
   print(response.read())
   connection.close()

def addhttp():
    json1={"cmd":122,"method":"GET","language":"CN","sessionId":"a608305057107c037c3fa2504dcf81875f4b48f5a49b734207fe3c101c4f5855"}
    r = requests.post('http://192.168.19.1/cgi-bin/http.cgi', json=json1)
    //print(r.status_code)
    print(r.json())


if __name__ == '__main__':
    if(len(sys.argv) == 1):
        addhttp()
    else:
	    addit(sys.argv[1], sys.argv[2], sys.argv[3])
