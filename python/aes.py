#!/usr/bin/python
# -*- coding: UTF-8 -*-

#if something wrong ,try this.
#sudo apt install python-pip

import sys
import os
import datetime
import md5
import commands
from Crypto.Cipher import AES

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

def sumfile(fobj):   
    m = md5.new()
    while True:
        d = fobj.read(8096)
        if not d:
            break
        m.update(d)
    return m.hexdigest()


def md5sum(fname):   
    if fname == '-':
        ret = sumfile(sys.stdin)
    else:
        try:
            f = file(fname, 'rb')
        except:
            return 'Failed to open file'
        ret = sumfile(f)
        f.close()
    return ret
	

def sendmail(afileName):
	sender = 'jianliang@sztozed.net'
	receivers = 'jianliang@139.com'
	message = MIMEMultipart()
	#message['Date'] = datetime.datetime.now().strftime('%c')
	(status, output) = commands.getstatusoutput('date -R')
	message['Date'] = output
	message['From'] = Header("jianliang@sztozed.net", 'ascii')
	message['To'] =  Header("jianliang@139.com", 'ascii')
	subject = afileName + datetime.datetime.now().strftime(' %Y-%m-%d %H:%M:%S')
	message['Subject'] = Header(subject, 'utf-8')
	message.attach(MIMEText("hello world! "+md5sum(afileName), 'plain', 'utf-8'))
	att1 = MIMEText(open(afileName, 'rb').read(), 'base64', 'utf-8')
	att1["Content-Type"] = 'application/octet-stream'
	# 这里的filename可以任意写，写什么名字，邮件中显示什么名字
	att1["Content-Disposition"] = 'attachment; filename='+afileName
	message.attach(att1)
	smtpObj = smtplib.SMTP() 
	smtpObj.connect("mail.sztozed.net", 25)  
	smtpObj.login("jianliang@sztozed.net", "tellmemore")  
	smtpObj.sendmail(sender, receivers, message.as_string())


def encode(afileName):
  obj = AES.new('This is a key123', AES.MODE_CBC, 'This is an IV456')
  org_fiile = open(afileName, 'r')
  message = org_fiile.read()
  length = 16 - (len(message) % 16)
  message += ' '*length
  ciphertext = obj.encrypt(message)
  #print ciphertext
  ace_file = open(os.path.splitext(afileName)[0]+'.bin', 'w')
  ace_file.write(ciphertext)

def decode(afileName):
  obj2 = AES.new('This is a key123', AES.MODE_CBC, 'This is an IV456')
  ace_file = open(afileName, 'r')
  message = ace_file.read()
  orgtext = obj2.decrypt(message)
  org_fiile = open(os.path.splitext(afileName)[0]+'.txt', 'w')
  org_fiile.write(orgtext)


if __name__ == '__main__':
	if sys.argv[1] == 'encode':
		encode(sys.argv[2])
	elif sys.argv[1] == "decode":
		decode(sys.argv[2])
	elif sys.argv[1] == "mail":
		sendmail(sys.argv[2])
	else:
		print "what???"
