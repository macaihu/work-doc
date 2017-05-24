#!/usr/bin/python
# -*- coding: utf-8 -*-
import telnetlib
import time

host='192.168.1.1'
username='root'
password='Tztopap1234'
finish='#'


def reboot():
	print("conneting...")
	tn = telnetlib.Telnet(host)

	#print tn.read_until('login:')

	#tn.write(username + '\n')
	#print tn.read_until('Password:')
	#tn.write(password + '\n')
	print tn.read_until(finish)
	tn.write('ps\n')
	print tn.read_until(finish)
	tn.write('reboot\n')
	print tn.read_until(finish)

	tn.close()

count=0;
while 1 :
	count = count+1
	print "reboot %d times" %count
	reboot()
	time.sleep(80)
