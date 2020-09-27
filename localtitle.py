
import requests, sys
import threading
import sys, os, re, time, socket
from Queue import *
from sys import stdout
from bs4 import BeautifulSoup as bs
print("____________________ROUTER SCAN____________________")
#def tittle_scan(ip):
#	try:
#		url = ("http://" + ip + "/")
#		r = requests.get(url)
#		soup = bs(r.content, 'lxml')
#		title = (soup.select_one('title').text)
#	except:
#		print("HTTP DOWN")
#		pass
input_file = open(sys.argv[1])
port = sys.argv[2]
def loligang(input_file):
	#input_file = open(sys.argv[1])
	for i in input_file.readlines():
		ip = i.strip("\n")
		try:
			url = ("http://" + ip + ":" + port +"/")
			r = requests.get(url, timeout=6, verify=True)
			soup = bs(r.content, 'lxml')
			title = (soup.select_one('title').text)
			print(url + " " + title)
			kkk = open("servers.txt", "a").write(ip + " " + title + "\n")
		except:
			pass
	input_file.close()
if __name__ == "__main__":
	loligang(input_file)
#x = threading.Thread(target=loligang, args=(1,))
	#print("Thread debug")
	#x.start()
	#print(threading.enumerate())
