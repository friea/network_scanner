#!/usr/bin/python
from scapy.all import *
def(self, ip):
	TIMEOUT = 2
	conf.verb = 0
   	paket = IP(dst=ip, ttl=20)/ICMP()
    	cevap = sr1(paket, timeout=TIMEOUT)
    	if not (cevap is None):
         	print cevap.dst, " aktif"
    	else:
         	print "%s -> Zaman aşımı" %paket[IP].dst