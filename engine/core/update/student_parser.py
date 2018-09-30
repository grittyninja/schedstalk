#!/usr/bin/python
""" 
Jumlah Mahasiswa IPB Aktif : 13617
Waktu eksekusi : 461.461788177 detik / 7 menit 41 detik

Last time Running 17 Desember 2015, 21:41 - 21:49
"""

import urllib2 as ulib
from bs4 import BeautifulSoup as bsoup 
from allmk import *
from time import sleep 
import sys 
import timeit
start = timeit.default_timer()
def print_waktu(waktu):
	waktu = float(waktu)
	menit = int(waktu // 60)
	detik = waktu % 60
	if(menit>0):
		print str(menit) + " menit",
	if(detik>0):
		print str(detik) + " detik"
students = []
visited = 0
Error_Message = ""
print "\n\n::: Get Student Data :::\n"
for mk in matkul:
	try:
		visited += 1
		progress = round(visited/float(len(matkul))*100,2)
		sys.stdout.write('\r')
		sys.stdout.write("[%-100s] %.2f%%" % ('='*int(progress), progress))
		sys.stdout.flush()
		
		url_jadwal = "http://krs.ipb.ac.id/krs/viewmk/mk/" + mk
		html = ulib.urlopen(url_jadwal)
	
		soup = bsoup(html, 'html.parser')
	
		table_tag = soup.find("table",{"class":"table-bordered"})
		a_tag = table_tag.find_all("a")
		for sched in a_tag:
			url_student = "http://krs.ipb.ac.id/" + str(sched["href"])
			html2 = ulib.urlopen(url_student)
			soup2 = bsoup(html2, 'html.parser')
			li_tag = soup2.find_all("li")
			for data in li_tag:
				parsed_nim = str(data.text)
				NIM = parsed_nim[parsed_nim.index('[')+1:parsed_nim.index(']')].lower()
				Fullname = parsed_nim[parsed_nim.index(']')+2:len(parsed_nim)-1].lower()
				students.append([NIM,Fullname])
	except:
		Error_Message += "\n[ERROR] MK Code : " + mk
students = list(set(tuple(item) for item in students))
print "" # null
if(Error_Message != ""):
	print "\n---- Error Messages ----"
	print Error_Message
	print "-----------------------"
print "\nJumlah Mahasiswa IPB Aktif :", len(students)
students.sort()

file = open("studentList.py", 'w')
file.write("students = ")
file.write(str(students))
file.close()
stop = timeit.default_timer()
print "\nWaktu eksekusi :", 
print_waktu(str(stop - start))