#!/usr/bin/python
from socket import *
import re
import thread
import sys
import time
time_dues = {}                                                                         #holds time of diffrent threads   connection id: timedue
active_connections = {}                                                                #active connection IDs     connection id : 0 , could have been list
timestamps={}                                                                          # thread_id:activation_time         connection id : timestamp
addresses = {}                                                                         # connection id : addresses
def kill(y):
	connection=addresses[y]
	connection.sendall('{"status":"kill"}\n')                                          #send the status to be killed
	connection.close()                                                                 #close the connection
	active_connections.pop(y)                                                          #now refresh database
	time_dues.pop(y)
	timestamps.pop(y)
	addresses.pop(y)
	return                                                                             #return to parent as we are supposed to send whether command was success or not
	

def newConnection(connection,addr,y):                                                  #takes connection,addr,and y uis a list containg connection id and timeout
	if y[0] in active_connections.keys():
		connection.sendall("connection already active\n")                              #if connection already active
		connection.close()
	else :
		active_connections[y[0]] = 0   							                       #update the databse
		time_dues[y[0]] = y[1]     												
		timestamps[y[0]]=int(time.time())
		addresses[y[0]]=connection
	time.sleep(float(y[1])) 								                           #wait for the process to get completed
	connection.sendall('{"status":"ok"}\n');                                           #send ok after completition pf process
	time_dues.pop(y[0])                                                                #now update the database
	timestamps.pop(y[0])
	addresses.pop(y[0])
	active_connections.pop(y[0])
	connection.close()                                       						   #close conection and exit thread
	sys.exit()




def serverStatus(connection,addr):
	running = {}
	for i in active_connections.keys():
		running[i] = str(int(time_dues[i])-(int(time.time())-int(timestamps[i])))      # provides remaining time of each thread 
	connection.sendall(str(running))
	connection.sendall("\n")
	connection.close()
	sys.exit()                                                                         #exit thread

def killConnection(connection,addr,y):
	if y in active_connections.keys():												   #if connection is active then kill
		kill(y)
		connection.sendall('{"status":"ok"}\n')
	else:																			   #if connection is not active ten raise error
		connection.sendall('"status":"invalid connection Id: '+y+'"\n')
	connection.close()
	sys.exit()



def serve(connection,addr):                                                             
	data=connection.recv(1024)
	data=data.rstrip('\n')
	l=len(data)
	data=data[0:l-1]																   #remove \n from data
	if re.match('^GET api/request\?connId=[0-9]+&timeout=[0-9]*$',data,flags=0):       #if data for new request
		print "request to run service\n"
		#connection.sendall("you want to run service")
		try:
			newConnection(connection,addr,re.findall("[0-9]+",data))                   #try to generate new request
		except Exception, e:
			raise e
			



	elif re.match('^GET api/serverStatus$',data,flags=0):                              #request to server status
		print "request to server status\n"
		#connection.sendall("you want server status\n")
		serverStatus(connection,addr)


	elif re.match('^PUT api/kill\?connId=[0-9]+$',data,flags=0):                       #request to kill a process
		print "request to kill service\n"
		#connection.sendall("you want to kill service\n")
		y=re.findall("[0-9]+",data)

		killConnection(connection,addr,y[0])


	else:
		print 'no such service\n'                                                      # raise error if wrong request is made
		connection.sendall("no such service\n")
	#connection.sendall('\n')
	connection.close()
	sys.exit()
if len(sys.argv) != 2:
	print 'USAGE python server.py <port>'
	exit(0)
port=int(sys.argv[1])

mysock = socket(AF_INET,SOCK_STREAM)                                                   #start listening on localhost
mysock.bind(('127.0.0.1',port))    
print 'server running at 127.0.0.1:',port                                       
mysock.listen(1000)                                                                
while True:
	conn,addr = mysock.accept()
	print 'connected with '+addr[0]+':'+str(addr[1])
	conn.sendall('we support following requests\nGET api/serverStatus\nGET api/request?connId=<connection_id>&timeout=<time>\nPUT api/kill?connId=<connection_id>\n\n')
	thread.start_new_thread(serve,(conn,addr))                                         #generate new thread