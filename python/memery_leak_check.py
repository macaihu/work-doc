#!/usr/bin/python
# -*- coding: utf-8 -*-


#pip install paramiko
import paramiko  
import time
import sys
import os
	
def sshclient_execmd(hostname, port, username, password, execmd):  
	paramiko.util.log_to_file("paramiko.log")  
	s = paramiko.SSHClient()  
	s.set_missing_host_key_policy(paramiko.AutoAddPolicy())  
	s.connect(hostname=hostname, port=port, username=username, password=password)  
	stdin, stdout, stderr = s.exec_command (execmd)  
	stdin.write("Y")  # Generally speaking, the first connection, need a simple interaction.  
	print stdout.read()  
	s.close()  

def read_info(s,hostname):
	stdin, stdout, stderr = s.exec_command ('uptime')  
	print stdout.read()
	stdin, stdout, stderr = s.exec_command ('ls /tmp/coredump')  
	#stdin.write("Y")  # Generally speaking, the first connection, need a simple interaction.  
	coredumpfiles = stdout.read() 
	if(coredumpfiles==""):
		print "ok no crash files"
	else:
		os.system("sshpass -p sztz369147258 scp -P 8357 root@" + hostname + ":/tmp/coredump/* .")
		print coredumpfiles
	stdin, stdout, stderr = s.exec_command ('cat /proc/meminfo | grep MemFree')  
	print stdout.read()	
	stdin, stdout, stderr = s.exec_command ('dmesg -c')  
	print stdout.read()	

def check_error(hostname, port, username, password):
	#paramiko.util.log_to_file("paramiko.log")  
	s = paramiko.SSHClient()  
	s.set_missing_host_key_policy(paramiko.AutoAddPolicy())  
	s.connect(hostname=hostname, port=port, username=username, password=password)  
	while(True):
		read_info(s, hostname)
		time.sleep(30)
	s.close()  	

def main(host):
	port = 8357
	username = 'root'  
	password = 'sztz369147258'  
	check_error(host , port, username, password)  
	#check_error("192.168.19.3" , port, username, password)  


if __name__ == '__main__':
	main(sys.argv[1])

