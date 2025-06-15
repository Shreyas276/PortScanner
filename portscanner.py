import socket
import termcolor

def scan(target,ports):
	print('\n' + ' Starting Scan For ' + str(target))
	for port in range(1,ports):
		scan_port(target,port)

def scan_port(ipaddress,port):
	try:
		sock = socket.socket()
		sock.connect((ipaddress,port))
		print("[+] Port Opened " + str(port))
		sock.close()
	except:
		pass

targets = input("[*] Enter Targets To Scan(Split Them by ,): ")
ports = int(input("[*] Enter How Many Ports To Be Scanned: "))

if ',' in targets:
	print(termcolor.colored(("[+] Scanning Multiple Targets--"), 'red'))
	for ip_addr in targets.split(','):
		scan(ip_addr.strip(' '),ports)
else:
	scan(targets,ports)
