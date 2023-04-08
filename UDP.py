#! /usr/bin/python

import logging
logging.getLogger(“scapy.runtime”).setLevel(logging.ERROR)
from scapy.all import *


def udp_scan(dst_ip,dst_port,dst_timeout):
	cevap= sr1(IP(dst=dst_ip)/UDP(dport=dst_port),timeout=dst_timeout)
	if (str(type(cevap))==”<type ‘NoneType’>”):
		cevaplar = []
		for count in range(0,3):
			cevaplar.append(sr1(IP(dst=dst_ip)/UDP(dport=dst_port),timeout=dst_timeout))
		for i in cevaplar:
			if (str(type(i))!=”<type ‘NoneType’>”):
				udp_scan(dst_ip,dst_port,dst_timeout)
				return “Açık|Filtreli”
			elif (cevap.haslayer(UDP)):
				return “Açık”
			elif(cevap.haslayer(ICMP)):
				if(int(cevap.getlayer(ICMP).type)==3 and int(cevap.getlayer(ICMP).code)==3):
					return “Kapalı”
				elif(int(cevap.getlayer(ICMP).type)==3 and int(cevap.getlayer(ICMP).code) in [1,2,9,10,13]):
					return “Filtreli”

udp_scan(dst_ip,dst_port,dst_timeout)