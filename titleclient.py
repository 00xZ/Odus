import sys, socket, select
import requests
import threading
import os, re, time, socket
from Queue import *
from sys import stdout
from bs4 import BeautifulSoup as bs
host = "127.0.0.1"
port = 9099
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(2)
input_file = open(sys.argv[1])
porthttp = "80"
try :
	s.connect((host, port))
	print("[+] CONNECTED Odus CNC [+]")
except :
	print ('[!] Server is down [!]')
	sys.exit()
def loligang(input_file):
	for i in input_file.readlines():
		ip = i.strip("\n")
		try:
			url = ("http://" + ip + ":" + porthttp +"/")
			r = requests.get(url, timeout=6, verify=True)
			try:
				soup = bs(r.content, 'lxml')
				title = (soup.select_one('title').text)
				if title == "":
					print("NO TITLE")
				else:
					msg = (url + " " + title)
					print(msg)
					s.send(msg)
					kkk = open("servers_locallog", "a").write(ip + " " + title + "\n")
			except:
				pass
		except:
			pass
		input_file.close()
if __name__ == "__main__":
	loligang(input_file)
