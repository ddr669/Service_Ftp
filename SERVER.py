from socket import *
from time import sleep
from sys import argv
global S;
global IP,PORT;
IP = "192.168.0.3"
PORT = 4040
S = socket(AF_INET,SOCK_STREAM)
def MSGS():
	if(argv[-1] == "-c"):
		def sendMsg(msg):
			msgd = msg
			
			S.connect((IP,PORT))
			S.send(bytes(msgd.encode("UTF-8"))) #bytes(msg.encode('UTF-8')))
			S.close()				

	else:
		def sendMsg(msg):
			S.bind((IP,PORT))
			S.listen(5)
			while(True):
				cliente, addr = S.accept()
				print(cliente.recv(1024))
				cliente.close()

	sendMsg(input("ENVIE A MSG> "))
	

input()