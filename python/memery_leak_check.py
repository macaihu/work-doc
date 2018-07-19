#!/usr/bin/python
# -*- coding: utf-8 -*-

from pexpect  import pxssh

host='192.168.19.3'
user='root'
password='sztz369147258'


def connect(hostname, usrname, password):
  try:
    s=pxssh.pxssh()
    s.login(hostname, usrname, password)
    return s
  except Exception, e:
  	print "[-] Erro connecting:" + str(e)

def send_command(ssh_session, command1):
	ssh_session.sendline(command1)
	ssh_session.prompt()
	print ssh_session.before
	
session = connect(host, user, password)
def main():
	send_command(session, 'ls /')


if __name__ == '__main__':
	main()

