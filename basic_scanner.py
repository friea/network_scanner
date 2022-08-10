#!/usr/bin/env python
# -*- coding: utf-8 -*-
  

#kütüphanelerin eklenmesi
import socket
import time
import threading
from queue import Queue
import os
import platform
from datetime import datetime

socket.setdefaulttimeout(0.25)
print_lock = threading.Lock()

#hedefin IP bilgisi elde ediliyor
hedef = input('Taranacak host bilgisini giriniz: ')
t_IP = socket.gethostbyname(hedef)
print ('Host taraması başlatılıyor: ', t_IP)

#Açık olan portlar belirleniyor
def portscan(port):
   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   try:
      con = s.connect((t_IP, port))
      with print_lock:
         print(port, 'Açık')
      con.close()
   except:
      pass

#işlemin daha kısa sürede gerçekleştirilmesi için thread kullanılıyor
def threader():
   while True:
      thread = q.get()
      portscan(thread)
      q.task_done()
      
q = Queue()
startTime = time.time()
   
for x in range(100):
   t = threading.Thread(target = threader)
   t.daemon = True
   t.start()
   
for thread in range(1, 500):
   q.put(thread)
   
q.join()
#geçen süre ekrana bastırılıyor
print('Süre:', time.time() - startTime)
#ping fonksiyonu
def pingMode():
	net = input("Ağ adresini giriniz: ")
	net1= net.split('.')
	a = '.'

	net2 = net1[0] + a + net1[1] + a + net1[2] + a
	st1 = int(input("başlangıç : "))
	en1 = int(input("Bitiş : "))
	en1 = en1 + 1
	oper = platform.system()

	if (oper == "Windows"):
		ping1 = "ping -n 1 "
	elif (oper == "Linux"):
		ping1 = "ping -c 1 "
	else :
		ping1 = "ping -c 1 "
	t1 = datetime.now()
	print ("İlerleme:")

	for ip in range(st1,en1):
		addr = net2 + str(ip)
		comm = ping1 + addr
		response = os.popen(comm)
   
		for line in response.readlines():
			if(line.count("TTL")):
				break
			if (line.count("TTL")):
				print (addr, " ktif")
         
	t2 = datetime.now()
	total = t2 - t1
	print ("Tamamlanma süresi: ",total)
