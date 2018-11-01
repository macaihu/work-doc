#!/usr/bin/python
# -*- coding: utf-8 -*-


#pip install paramiko
import paramiko  
import time
import sys
import os

def show_wait(delay):
        print "wait %d sec." %delay
        for i in range(1, delay):
                sys.stdout.write('.')
                sys.stdout.flush()
                time.sleep(1)

def read_info(s,hostname):
	all_ok = False
	stdin, stdout, stderr = s.exec_command ('ps | grep switchwan | grep -v grep')  
	switchwan_exists = stdout.read()
	print switchwan_exists
	#print switchwan_exists.find('switchwan')
	if( switchwan_exists.find('switchwan') == -1 ):
		print 'switchwan not found!'
		s.exec_command('cat  /tmp/.switchwan')
		print stdout.read()
		sys.exit()
	stdin, stdout, stderr = s.exec_command ('ifconfig l2tp | grep inet')  
	l2tp_exists = stdout.read()	
	print l2tp_exists
	if( l2tp_exists.find('inet') == -1 ):
		print 'l2tp not connect!'
		sys.exit()
	stdin, stdout, stderr = s.exec_command ('route -n ')  
	print stdout.read()
	stdin, stdout, stderr = s.exec_command ('reboot')  
	#stdout.read()	

def check_error(hostname, port, username, password):
	#paramiko.util.log_to_file("paramiko.log")  
	while(True):
		s = paramiko.SSHClient()  
		s.set_missing_host_key_policy(paramiko.AutoAddPolicy())  
		s.connect(hostname=hostname, port=port, username=username, password=password)  
		read_info(s, hostname)
		show_wait(5*30)
		print ''
	s.close()  	

def main(host):
	port = 8357
	username = 'root'  
	password = 'sztz369147258'  
	check_error(host , port, username, password)  

if __name__ == '__main__':
	main(sys.argv[1])

