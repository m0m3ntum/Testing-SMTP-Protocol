import sys,socket,time

def sendServerMessage( message_to_send ,s):
	"This check the server's message and the it send it"
	while 1:
		s.send(message_to_send)    
		server_msg=s.recv(1024)
		if(server_msg[0]=='4'):
			print "Persistent Transient Failure:\n"
			value = 0;		
			while((value != 1) or (value != 2)):		
				value = raw_input("Press 1 for waiting 30 secs or 2 to exit: ")
		
			if(value==1):
				time.sleep(30)
			else:
				s.close()
				sys.exit(1)
		elif(server_msg[0]=='5'):
			print server_msg
			print "Permanent Failure! Program will end!\n"
			s.close()
			sys.exit(1)
		else:
			return server_msg#Here all ok.exit function





try: #here we try to connect to the server. if not we get an exception
	s=socket.socket()    
	s.connect(('mail.teiath.gr',25))    
except socket.error, (message):#Here we get the exception, if any
	if s:
		s.close()
	print "The Socket could not be opened!!! Reason: " , message
	sys.exit(1) #exit of the program
print 'Connection with the server established!\n'


server_msg=s.recv(1024)    
print server_msg

message_to_send = "EHLO gmx\r\n"   
server_msg = sendServerMessage( message_to_send ,s)    
print server_msg    


From=raw_input("Insert Mail From: ") 
#From = 'isicg14110@teiath.gr'      
message_to_send = "MAIL FROM: <"+From+">\r\n"
server_msg = sendServerMessage( message_to_send ,s)    
print server_msg    


To=raw_input("TO:")  
#To = 'fotisgalanis@hotmail.com' 
message_to_send = "RCPT TO: <"+To+">\r\n"   
server_msg = sendServerMessage( message_to_send ,s)    
print server_msg  


message_to_send = "DATA\r\n"    
server_msg = sendServerMessage( message_to_send ,s)    
print server_msg    


Subject=raw_input("Subject: ")    
Text=raw_input("Message:")    
message_to_send = "Subject: "+Subject+"\r\n\r\n"+Text+"\r\n.\r\n"
server_msg = sendServerMessage( message_to_send ,s)    
print server_msg

s.send("QUIT\r\n")
server_msg=s.recv(100000)   
print server_msg
   
s.close()
