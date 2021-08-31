# Odus
work in progress (Proof Of Concept)


LEGAL DISCLAIMER: *


 main_scan.sh is the loop
 
 
 
 todo: add CNC server.
 
 
 Hows it work: 
 
* main_scan.sh - runs main loop of scanning for http servers; 
* getting the title using titleclient.py;
* then adds exploitible routers to a SERVER_files


Now loaderpar.py loads the lists of servers ageints exploit scripts(directory /RCE/xxxxx.py where you have to custom set a exploit script(already have a few i made public on here)


thats what works.

.
what doesnt fully work. The scanning command & control server. basiclly have multipule computers run the scanning loop then connect it all back to a server which leave a html output and also parses everything to SERVER_files. why doesnt it work; it writes everything from previous loop scans again, leading to server crash bc that shit builds up fast its ^2 every loop run with like 4 pc itll crash in seconds so feel free to pull request this and give it some work. also wordpress scanner is fuct. ik why just dont care enough to fix it



localtitlev2.py: checks for dns and runs sqleye check
