#!/usr/bin/python
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

print "\n\n::: Get All Matkul Data (Prasyarat) :::\n"

matkul_data = []
visited = 0
Error_Message = ""
for mk in matkul:
	try:
		visited += 1
		progress = round(visited/float(len(matkul))*100,2)
		sys.stdout.write('\r')
		sys.stdout.write("[%-100s] %.2f%%" % ('='*int(progress), progress))
		sys.stdout.flush()
		mk_temp = []
		prasyarat_temp = []
		mk_temp.append(mk.lower())
		url_matkul = "http://krs.ipb.ac.id/krs/viewmk/mk/" + mk
		html = ulib.urlopen(url_matkul)
		soup = bsoup(html, 'html.parser')
		div_tag = soup.find("div",{"class":"panel-heading"})
		nama_matkul = div_tag.text
		strip = nama_matkul.index('-')
		nama_matkul = str(nama_matkul[strip+2:]).replace("  ","").replace("\n","")
		mk_temp.append(nama_matkul.lower())
		try:
			ol_tag = soup.find("ol")
			li_tag = ol_tag.find_all("li")
			for prasyarat in li_tag:
				prasyarat_temp.append(str(prasyarat.text)[:-1].lower())
		except:
			pass
		mk_temp.append(prasyarat_temp)
	  	matkul_data.append(mk_temp)
	except:
		Error_Message += "\n[ERROR] MK Code : " + mk

print ""

if(Error_Message != ""):
	print "\n\n---- Error Messages ----"
	print Error_Message
	print "-----------------------"
	
file = open("mkList.py", 'w')
file.write("matkuls = ")
file.write(str(matkul_data))
file.close()

stop = timeit.default_timer()
print "\nWaktu eksekusi :", 
print_waktu(str(stop - start))