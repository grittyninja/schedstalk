#!/usr/bin/python
import urllib2 as ulib
from bs4 import BeautifulSoup as bsoup 
from deplist import *
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

mklist = []
visited = 0
Error_Message = ""
print "\n\n::: Get All Available Matkul :::\n"
for departement in departements:
	try:
		visited += 1
		progress = round(visited/float(len(departements))*100,2)
		#print str(round(visited/float(len(departements))*100,2))+"%"
		sys.stdout.write('\r')
		sys.stdout.write("[%-100s] %d%%" % ('='*int(progress), progress))
		sys.stdout.flush()
	    
		# initiate url and get html source
		url_jadwal = "http://krs.ipb.ac.id/krs/jadwaldep?dep=" + departement
		html = ulib.urlopen(url_jadwal)
		
		soup = bsoup(html, 'html.parser')
		
		# get a tag inside table tags
		table_tag = soup.find("table")
		a_tag = table_tag.find_all("a")
		for mk in a_tag:
			mklist.append(mk.string)
	except:
		Error_Message += "\n[ERROR] Dept Code : " + departement

if(Error_Message != ""):
	print "\n\n---- Error Messages ----"
	print Error_Message
	print "-----------------------"
	
mklist = list(set(mklist))
mklist.sort()
mklist = [str(mk) for mk in mklist]

file = open("allmk.py", 'w')
file.write("matkul = ")
file.write(str(mklist))
file.close()

stop = timeit.default_timer()
print "\nWaktu eksekusi :", 
print_waktu(str(stop - start))