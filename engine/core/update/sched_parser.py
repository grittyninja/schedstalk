#!/usr/bin/python

import urllib2 as ulib
from bs4 import BeautifulSoup as bsoup 
from allmk import *
from time import sleep 
import sys 
import timeit
start = timeit.default_timer()
schedules = []
print "\n\n::: Get All Schedules :::\n"
def print_waktu(waktu):
	waktu = float(waktu)
	menit = int(waktu // 60)
	detik = waktu % 60
	if(menit>0):
		print str(menit) + " menit",
	if(detik>0):
		print str(detik) + " detik"
visited = 0
i, j, k = 0, 0, 0 # index untuk generate kode setiap kelas yakni kuliah, responsi, dan praktikum
Error_Message = ""
for mk in matkul:
	try:
		visited += 1
		progress = round(visited/float(len(matkul))*100,2)
		sys.stdout.write('\r')
		sys.stdout.write("[%-100s] %.2f%%" % ('='*int(progress), progress))
		sys.stdout.flush()
		
		class_stat = 0
		sched_temp = [mk.lower()]
		daylist = [" Minggu ", " Senin "," Selasa "," Rabu "," Kamis "," Jum'at "," Sabtu "]
		url_jadwal = "http://krs.ipb.ac.id/krs/viewmk/mk/" + mk
		html = ulib.urlopen(url_jadwal)
	
		soup = bsoup(html, 'html.parser')
		for day in daylist:
			day = day.replace(" ","")
			if day in soup.text:
				class_stat = 1
				break
	
		table_tag = soup.find("table",{"class":"table-bordered"})
		tbody_tag = table_tag.find("tbody")
		tr_tag = tbody_tag.find_all("tr")
		class_temp = []
		data_temp = []
		room_temp = []
		c = len(tr_tag)
		for data in tr_tag:
			if(("\n" not in str(data.text))):
				if(data_temp == []):
					data_temp = [str(daylist.index(str(data.text)))]
				else:
					data_temp.append(room_temp)
					class_temp.append(data_temp)
					data_temp = [str(daylist.index(str(data.text)))]
					room_temp = []
			else:
				if(not(class_stat)):
					data_temp = ['0'] # kondisi kuliah tanpa jadwal 
				
				# mendapatkan link peserta untuk ditelusuri
				href = data.find("a",{"href":True})
				
				# dapatkan nim peserta pengambil kelas (Kuliah, Responsi, atau Praktikum)
				NIMs = []
				url_student =  "http://krs.ipb.ac.id" + str(href['href'])
				nimsource = ulib.urlopen(url_student)
				soup2 = bsoup(nimsource, 'html.parser')
				li_tag = soup2.find_all("li")
				for li in li_tag:
					parsed_nim = str(li.text)
					NIM = parsed_nim[parsed_nim.index('[')+1:parsed_nim.index(']')].lower()
					NIMs.append(NIM)
				data = str(data.text)
				
				# dapatkan informasi per baris jadwal
				datastruct = data[1:-1].split('\n')
	
				# generate kode kelas
				if("Kuliah" in datastruct[0]):
					i += 1
					kodekelas = "K"+str(i)
				elif("Responsi" in datastruct[0]):
					j += 1
					kodekelas = "R"+str(j)
				elif("Praktikum" in datastruct[0]):
					k += 1
					kodekelas = "P"+str(k)
	
				# dapatkan informasi yang dibutuhkan
				mulai = datastruct[1]
				selesai = datastruct[2]
				ruangan = datastruct[3]
	
				room_temp.append([kodekelas,ruangan,mulai,selesai,NIMs])
				
				if(c == 1): # end of loop 
					data_temp.append(room_temp)
					class_temp.append(data_temp)
			c -= 1
		
		sched_temp.append(class_temp)
		schedules.append(sched_temp)
	except:
		Error_Message += "\n[ERROR] MK Code : " + mk

print ""

if(Error_Message != ""):
	print "\n\n---- Error Messages ----"
	print Error_Message
	print "-----------------------"
	
# write them down !
file = open("scheduleData.py", 'w')
file.write("data = ")
file.write(str(schedules))
file.close()

stop = timeit.default_timer()
print "\nWaktu eksekusi :", 
print_waktu(str(stop - start))
