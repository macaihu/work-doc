#!/usr/bin/python
# -*- coding: utf-8 -*-
import telnetlib
import time

host='10.8.0.103'
username='root'
password='Tztopap1234'
finish='#'


def reboot():
	print("conneting...")
	tn = telnetlib.Telnet(host)

	print tn.read_until('login:')

	tn.write(username + '\n')
	print tn.read_until('Password:')
	tn.write(password + '\n')
	print tn.read_until(finish)
	tn.write('ps\n')
	print tn.read_until(finish)
	tn.write('reboot\n')
	print tn.read_until(finish)

	tn.close()

while 1 :
	reboot()
	time.sleep(30)
