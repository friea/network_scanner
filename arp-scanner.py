#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  arp-scanner.py
#  
#  Copyright 2022 friea <friea@epsilon>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  


import scapy.all as scapy

class tara:
    def Arp(self, ip):
        self.ip = ip
        print(ip)
        arp_r = scapy.ARP(pdst=ip) #arp sorgusunun ip adresini ayarlanır
        br = scapy.Ether(dst='ff:ff:ff:ff:ff:ff') #alıcı adresi broadcast olarak ayarlanır
        request = br/arp_r #2. ve 3.katman protokollerini birleştirir
        bayrak1, bayrak0 = scapy.srp(request, timeout=1, iface = 'wlp1s0', inter = 0.1) #isteği gönderir
        print('\tIP\t\t\t\t\tMAC') # sırayla ip ve mac adreslerini ekrana basar
        print('_' * 50)
        for i in bayrak1:
            ip, mac = i[1].psrc, i[1].hwsrc
            print(ip, '\t\t' + mac)
            print('-' * 50)

arp = tara() # tara sınıfı çağrılır
IP=input("Ağ adresini giriniz:")
arp.Arp(str(IP)) # Arp metodunu çağırır
