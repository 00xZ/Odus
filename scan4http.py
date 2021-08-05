import sys 
import random  
import pickle
print "\n +-+-+-+==+-+-+-+=Windows Zmap 80=+-+-+-+==+-+-+-+" #ikik it aint zmap but its a sub for it
import requests
import threading
import os, re, time, socket
port = 80
def scanner():
	ip = str(random.randrange(0,256))+'.'+str(random.randrange(0,256))+'.'+str(random.randrange(0,256))+'.'+str(random.randrange(0,256))
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.settimeout(1.5)
	result = sock.connect_ex((ip, port))
	sock.close()
	if result == 0:
		print("OPEN : " + ip)
		kkk = open("list.lst", "a").write(ip + "\n")
	else:
		pass
for x in range(0,10): #prolly didnt even do this right but fuck it it will be updated when i have time
	try:
		t = threading.Thread(target=scanner())
		threads.append(t)
		t.start()
	except:
		pass
