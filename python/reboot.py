#!/usr/bin/python
# -*- coding: utf-8 -*-
import telnetlib

host='10.8.0.103'
username='root'
password='Tztopap1234'
finish='#'

print("conneting...")
tn = telnetlib.Telnet(host)

print tn.read_until('login:')

tn.write(username + '\n')
print tn.read_until('Password:')
tn.write(password + '\n')
print tn.read_until(finish)
tn.write('ps\n')

print tn.read_until(finish)

tn.close()