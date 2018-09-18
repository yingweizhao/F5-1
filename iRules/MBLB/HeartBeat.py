# -*- coding: UTF-8 -*-
import socket 
import time

def get_input(describe,default):
	input_param = raw_input("%s (default: %s): " %(describe,default)).strip()
	if input_param is "":
		return default
	else:
		return input_param

host = get_input("sever_ip","127.0.0.1")
port = int(get_input("sever_port",8003))
send_times = int(get_input("send_times",10))
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.connect((host,port))
print "Connected to %s:%s." %(host,port)
i=1
while i<=send_times:
	s.send('0000')
	print 'Send num: %s' %i
	i+=1
	time.sleep(1)
s.close()
print "Connection closed."
