import sys,socket,base64,time,Image



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

   return server_msg

#Here all ok.exit function









####Main starting HERE####################################

try: #here we try to connect to the server. if not we get an exception

 s=socket.socket()    

 s.connect(('mail.domain.gr',25))    

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





#From=raw_input("Insert Mail From: ") 

From = 'user@domain.gr'      

message_to_send = "MAIL FROM: <"+From+">\r\n"

server_msg = sendServerMessage( message_to_send ,s)    

print server_msg    





#To=raw_input("TO:")  

To = 'user@otherdomain.gr' 

message_to_send = "RCPT TO: <"+To+">\r\n"   

server_msg = sendServerMessage( message_to_send ,s)    

print server_msg  





message_to_send = "DATA\r\n"    

server_msg = sendServerMessage( message_to_send ,s)    

print server_msg





######################

Text=raw_input("Message:")

#path=raw_input("Give image path:")

path="/home/user/test.jpg"

#message_to_send = "Subject: "+Subject+"\r\n\r\n"+Text+"\r\n.\r\n"





with open(path, "rb") as image_file:

    encoded = base64.b64encode(image_file.read())

image = "";

size = len(encoded)

i = 0

while i<size:

	if (i%77)>0:

		image += encoded[i]

	else:

		image += "\r\n"

	i=i+1



message_to_send = "MIME-Version: 1.0\r\n"   



Subject=raw_input("Subject:") 



message_to_send += "Subject: "+Subject+"\r\n"

message_to_send += "Content-type: multipart/mixed; boundary=\"AZERTYUIOP\";\r\n"

message_to_send += "Content-type=text/plain\r\n\r\n"

message_to_send += Text+"\r\n"

message_to_send += "--AZERTYUIOP\r\n"

message_to_send += "Content-Type: octet/stream; name=\"LAD-27.jpg\"\r\n"

message_to_send += "Content-transfer-encoding: base64\r\n"

message_to_send += image + "\r\n"

message_to_send += "--AZERTYUIOP--\r\n"

message_to_send += ".\r\n"



server_msg = sendServerMessage( message_to_send ,s)    

print server_msg



##########################



s.send("QUIT\r\n")

server_msg=s.recv(100000)   

print server_msg

   

s.close()
