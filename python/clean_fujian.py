#!/usr/bin/python
# -*- coding: utf-8 -*-
import telnetlib
import time
import sys

host=str(sys.argv[1])
username='root'
password='Ap8358'
#password="NZ%ttu6"
finish='#'


def clean_it():
	print("conneting...%s", host)
	tn = telnetlib.Telnet(host)
	print tn.read_until('login:')
	tn.write(username + '\n')
	print tn.read_until('Password:')
	tn.write(password + '\n')
	print tn.read_until(finish)
	tn.write('ps\n')
	print tn.read_until(finish)

#rm somefiles.
	tn.write('rm /.dvrConfig -rf\n')
	print tn.read_until(finish)
	tn.write('rm /dvrHelper -rf\n')
	print tn.read_until(finish)
	tn.write('rm /cquFttnts -rf\n')
	print tn.read_until(finish)
	tn.write('rm /dvrAssist -rf\n')
	print tn.read_until(finish)
	tn.write('rm /gmlocerfno -rf\n')
	print tn.read_until(finish)
	tn.write('rm /satori.bot -rf\n')
	print tn.read_until(finish)
	tn.write('rm /xhgyeshowm -rf\n')
	print tn.read_until(finish)
	tn.write('rm /usr/friend.* -rf\n')
	print tn.read_until(finish)
	tn.write('rm /usr/gmlocerfno -rf\n')
	print tn.read_until(finish)
	tn.write('rm /usr/satori.* -rf\n')
	print tn.read_until(finish)
	tn.write('rm /usr/xhgyeshowm -rf\n')
	print tn.read_until(finish)
	tn.write('rm /usr/elfDrp -rf\n')
	print tn.read_until(finish)
	tn.write('rm /tmp/dvrHelper -rf\n')
	print tn.read_until(finish)
	tn.write('rm /tmp/xhgyeshowm -rf\n')
	print tn.read_until(finish)
	tn.write('rm /tmp/dvrMoney -rf\n')
	print tn.read_until(finish)
	tn.write('rm /tmp/dropMoney -rf\n')
	print tn.read_until(finish)
	tn.write('rm /tmp/gmlocerfno -rf\n')
	print tn.read_until(finish)
	tn.write('rm /bin/c -rf\n')
	print tn.read_until(finish)
	tn.write('rm /bin/client -rf\n')
	print tn.read_until(finish)

#change password
	tn.write('passwd\n')
	print tn.read_until('New password:')
	tn.write('NZ%ttu6\n')
	print tn.read_until('Retype password:')
	tn.write('NZ%ttu6\n')
	print tn.read_until(finish)

#change telnetd port
	tn.write("sed  '102s/.*/\/usr\/sbin\/telnetd -p 30047/g'  -i /etc/rc.d/rcS\n")
	print tn.read_until(finish)
	tn.write('telnetd -p 30047\n')
	print tn.read_until(finish)

#kill curr telnetd.
	tn.write("CURR_TELNETD=$(ps | grep /usr/sbin/telnetd | cut -b 1-5)\n")
	curr_telnetd_pid=tn.read_until(finish)
	print curr_telnetd_pid
	tn.write("kill -9 ")
	tn.write(curr_telnetd_pid)
	tn.write("\n")
	print tn.read_until(finish)
	tn.close()

clean_it()
