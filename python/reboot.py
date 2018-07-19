#!/usr/bin/python
# -*- coding: utf-8 -*-
import telnetlib
import time

host='192.168.19.3'
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
	tn.write('iptables -S -t nat\n')
	readline = tn.read_until(finish)
	print readline
	findit = readline.find('DNAT')
	if ( findit == -1 ) :
		exit
	tn.write('reboot\n')
	print tn.read_until(finish)

	tn.close()

count=0;
while 1 :
	count = count+1
	print "reboot %d times" %count
	reboot()
	for loop in range(80):
		time.sleep(1)
		print '*',
