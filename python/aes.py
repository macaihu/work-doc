
# -*- coding: UTF-8 -*-

import sys
from Crypto.Cipher import AES

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

def sendmail():
	sender = 'jianliang@sztozed.net'
	receivers = 'jianliang@139.com'
	message = MIMEMultipart()
	message['From'] = Header("jianliang@sztozed.net", 'utf-8')
	message['To'] =  Header("jianliang@139.com", 'utf-8')
	subject = 'pass form jianliang'
	message['Subject'] = Header(subject, 'utf-8')
	message.attach(MIMEText("hello world", 'plain', 'utf-8'))
	att1 = MIMEText(open('pass', 'rb').read(), 'base64', 'utf-8')
	att1["Content-Type"] = 'application/octet-stream'
	# 这里的filename可以任意写，写什么名字，邮件中显示什么名字
	att1["Content-Disposition"] = 'attachment; filename="pass"'
	message.attach(att1)
	smtpObj = smtplib.SMTP() 
	smtpObj.connect("mail.sztozed.net", 25)  
	smtpObj.login("jianliang@sztozed.net", "tellmemore")  
	smtpObj.sendmail(sender, receivers, message.as_string())


def encode():
  obj = AES.new('This is a key123', AES.MODE_CBC, 'This is an IV456')
  org_fiile = open('pass.txt', 'r')
  message = org_fiile.read()
  length = 16 - (len(message) % 16)
  message += '\0'*length
  ciphertext = obj.encrypt(message)
  #print ciphertext
  ace_file = open('pass', 'w')
  ace_file.write(ciphertext)

def decode():
  obj2 = AES.new('This is a key123', AES.MODE_CBC, 'This is an IV456')
  ace_file = open('pass', 'r')
  message = ace_file.read()
  orgtext = obj2.decrypt(message)
  org_fiile = open('pass.txt', 'w')
  org_fiile.write(orgtext)


if __name__ == '__main__':
	if sys.argv[1] == 'encode':
		encode()
	elif sys.argv[1] == "decode":
		decode()
	elif sys.argv[1] == "mail":
		sendmail()
