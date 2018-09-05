#!/usr/bin/python
# -*- coding: utf-8 -*-


#pip install paramiko
import paramiko  
	
def sshclient_execmd(hostname, port, username, password, execmd):  
	paramiko.util.log_to_file("paramiko.log")  
	s = paramiko.SSHClient()  
	s.set_missing_host_key_policy(paramiko.AutoAddPolicy())  
	s.connect(hostname=hostname, port=port, username=username, password=password)  
	stdin, stdout, stderr = s.exec_command (execmd)  
	stdin.write("Y")  # Generally speaking, the first connection, need a simple interaction.  
	print stdout.read()  
	s.close()  
	
def check_error(hostname, port, username, password):
	#paramiko.util.log_to_file("paramiko.log")  
	s = paramiko.SSHClient()  
	s.set_missing_host_key_policy(paramiko.AutoAddPolicy())  
	s.connect(hostname=hostname, port=port, username=username, password=password)  
	stdin, stdout, stderr = s.exec_command ('ls /tmp/coredump')  
	#stdin.write("Y")  # Generally speaking, the first connection, need a simple interaction.  
	coredumpfiles = stdout.read() 
	if(coredumpfiles==""):
		print "ok no crash files"
	else:
		print coredumpfiles
	stdin, stdout, stderr = s.exec_command ('cat /proc/meminfo | grep MemFree')  
	print stdout.read()
	stdin, stdout, stderr = s.exec_command ('uptime')  
	print stdout.read()	
	s.close()  	

def main():
	#hostname = '192.168.19.3'  
	port = 8357
	username = 'root'  
	password = 'sztz369147258'  
	execmd = "ls /"  
	#sshclient_execmd(hostname, port, username, password, execmd)  
	check_error("192.168.19.1" , port, username, password)  
	check_error("192.168.19.3" , port, username, password)  


if __name__ == '__main__':
	main()

