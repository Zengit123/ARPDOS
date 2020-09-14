# ARPDOS
This python3 script creates a Denial Of Service (DOS) attack by flooding a network's gateway
with ARP requests using source IP of other devices, causing ARP conflicts which jams any network traffic.
<br />DISCLAIMER: ANY TYPE OF DENIAL OF SERVICE (DOS) IS ILLEGAL, PLEASE DO NOT USE THIS TOOL FOR ILLEGAL PURPOSES!<br /> <br />
WORKS ONLY WITH BASH!

#### Usage:
* If nothing is added, the script runs Nmap to find devices on its own. Keep in mind that Nmap can sometimes fail to discover devices.
* -add [IP address 1; IP address 2...] --- add a set of IP adresses to attack.
* -exclude [IP address 1; IP address2...] --- attack only the selected IP addresses.



#### Examples:
* To attack every device in the network:
```
sudo python3 arpdos.py
```

* To attack every device in the network and add extra IP's:
```
sudo python3 arpdos.py -add 192.168.0.101 192.168.0.105
```

* To attack specific devices in the network:
```
sudo python3 arpdos.py -exclude 192.168.0.54
```

#### Requirements:
* python3
* route
* ifconfig
* nmap
* arping
</pre>
