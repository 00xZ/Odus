clear
while true
do
	sudo zmap -N 15 -p 80 -o list.lst -B 100M -i wlan0
	python titleclient.py list.lst 80
	cat servers.txt | sort | uniq > DATABASE.txt
	cat servers.txt | grep Cisco > SERVER_files/Cisco_servers.lsd
	cat servers.txt | grep ZXHN > SERVER_files/ZXHN.lsd
	cat servers.txt | grep outer > SERVER_files/router_servers.lsd
	cat servers.txt | grep D-L > SERVER_files/d-link.lsd
	cat servers.txt | grep DSL > SERVER_files/dsl_servers.lsd
	cat servers.txt | grep etgear > SERVER_files/netgear_servers.lsd
	cat servers.txt | grep ogin > SERVER_files/login_sites.lsd
	cat servers.txt | grep TL- > SERVER_files/TL_servers.lsd
	cat servers.txt | grep outerOS > SERVER_files/mikrotik && cat SERVER_files/mikrotik | awk ' { print $1 } ' > SERVER_files/raw_MIKROTIK.lsd
	cat SERVER_files/*.lsd | awk ' { print $1 } ' > ROUTERS.lsd
done
