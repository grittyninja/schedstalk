#!/usr/bin/python
# classify every query #
import sys
import re, math
import time
import datetime
time = datetime.datetime.now()
sys.path.extend(['core','core/data'])
from random import randint
from timeit import default_timer
start = default_timer()
import studentSim, mkSim, correctQuery
quoted = re.compile('"[^"]*"')
query = sys.argv[1].lower()
days = {'0':'Minggu','1':'Senin','2':'Selasa','3':'Rabu','4':'Kamis','5':'Jumat','6':'Sabtu'}
strError = ["Maaf input yang kamu masukkan tidak dikenali", "sepertinya terjadi kesalahan pada query yang kamu masukkan, mohon cek kembali","sistem tidak dapat mengerti query yang kamu masukkan", "query yang kamu masukkan tidak dimengerti oleh sistem"]

def getTime(minute):
	hour = minute // 60
	minute = minute % 60
	minute = "%02d" % (minute,)
	return str(hour)+":"+str(minute)

def printsaran():
	print """<br><div style="margin-top:10px" class="left-align"> Saran :<ul><li>- Lihat contoh query yang sudah ada.</li><li>- Perbaiki kata-kata yang <i>typo</i>.</li><li><a href="https://drive.google.com/file/d/0B_kAnrNjT4xeNUp1eExXOEtIMHc/view?usp=sharing" target="_blank">- Download contoh penggunaan</a></li><li>- Lihat contoh <a href="latest/">kueri terbaru</a> yang berhasil dieksekusi.</li></ul>"""
def printerror():
	indexError = randint(0,len(strError)-1)
	print "<b>"+strError[indexError]+"</b>"
	printsaran()
	
# segmentation object
objects = quoted.findall(query)
if(len(objects)>2 or len(objects)<1 or len(query)>=120):
	printerror()
	sys.exit()

# object error correction
mkCount = 0
studentCount = 0
studentObject = []
mkObject = []

for object_ in objects:
	query.replace('"+object_+"',"")
	identify = 0
	mkCorrect = mkSim.sim(object_)
	studentCorrect = studentSim.sim(object_)
	if(mkCorrect):
		identify = 1
		mkCount += 1
		mkObject.append(mkCorrect)
		print "<sub><sub>menampilkan hasil untuk <b>"+ mkCorrect[1] + "</b> <sub>*kemiripan "+ str(round(mkCorrect[2]*100,2))+"%" +"</sub></sub></sub><br/><br/>"
	elif(studentCorrect):
		identify = 1
		studentCount += 1
		studentObject.append(studentCorrect)
	if(not(identify)):
		print "<b>"+object_+"</b> tidak dikenali oleh sistem."
		printsaran()
		sys.exit()

# Query Correction
correctedQuery, day, minute = correctQuery.correct(query)

# Time Correction
if(not(day)):
	daynow = time.weekday() + 1
	if(daynow == 7):
		daynow = 0
if(not(minute)):
	minutenow = time.hour * 60 + time.minute

print "<!--"+correctedQuery+"-->"

# Query Classification
if(studentCount == 1 and mkCount == 0):
	# 1, 4, 7, 8, 10
	qweight = [0,0,0,0,0]
	weight =  [["kosong", [0.5,-1,-1,-1,0.5]],["mana", [-1,1,-1,-1,-1]],["kapan", [-1,-1,-1,-1,1]],["hari", [0.2,0.3,0.6,-1,0.4]],["jam", [0.45,0.55,-1,-1,-1]],["sekarang", [0.45,0.55,-1,-1,-1]],["ruang", [-1,1,-1,-1,-1]],["tempat", [-1,1,-1,-1,-1]],["lokasi", [-1,1,-1,-1,-1]],["berikan", [-1,0,0,0,0]],["seluruh", [-1,-1,0.4,0.4,0.2]],["jadwal", [-1,-1,0.7,-1,0.3]],["mat", [0,0,0,1,0]],["ambil", [0,0,0,1,0]],["ikut", [0,0,0,1,0]],["apa", [0.4,-1,0.1,0.5,-1]]]
	for word in correctedQuery.split(' '):
		for w in weight:
			if w[0] in word:
				for i in range(5):
					qweight[i] = qweight[i] + w[1][i]
				break 
	print "<!--"+str(qweight)+"-->"
	choosen = qweight.index(max(qweight)) + 1
	if(choosen == 1):
		import spareTime
		if(not(day) and minute):
			output, status = spareTime.search(studentObject[0][0], daynow, minute)
			if(status):
				print "yap, <b>"+studentObject[0][1].title()+"</b> ["+studentObject[0][0].upper()+"] kosong pada hari ini jam <b>"+getTime(minute)+"</b>."
			else:
				print "<b>"+studentObject[0][1].title()+"</b> ["+studentObject[0][0].upper()+"] ada kegiatan kampus, "
				print output
		elif(day and minute):
			output, status = spareTime.search(studentObject[0][0], day, minute)
			if(status):
				print "yap, <b>"+studentObject[0][1].title()+"</b> ["+studentObject[0][0].upper()+"] kosong pada hari <b>"+days[str(day)]+"</b> jam <b>"+getTime(minute)+"</b>."
			else:
				print "<b>"+studentObject[0][1].title()+"</b> ["+studentObject[0][0].upper()+"] ada kegiatan kampus, "
				print output
				
		elif(day and not(minute)):
			import bulkSpareTime
			output = bulkSpareTime.lookup(studentObject[0][0], day)
			print 'Berikut seluruh jadwal kosong <b>'+studentObject[0][1].title()+'</b> ['+studentObject[0][0].upper()+'] pada hari :'
			print str(output)
		else:
			output, status = spareTime.search(studentObject[0][0], daynow, minutenow)
			if(status):
				print "yap, <b>"+studentObject[0][1].title()+"</b> ["+studentObject[0][0].upper()+"] kosong pada hari ini </b> jam <b>"+getTime(minutenow)+"</b>."
			else:
				print "<b>"+studentObject[0][1].title()+"</b> ["+studentObject[0][0].upper()+"] ada kegiatan kampus, "
				print output
			
	elif(choosen == 2):
		import locateMatkul
		if(minute and not(day)):
			output, status = locateMatkul.search(False, studentObject[0][0], minute, daynow)
		elif(not(minute) and not(day)):
			output, status = locateMatkul.search(False, studentObject[0][0], minutenow, daynow)
		elif(minute and day):
			output, status = locateMatkul.search(False, studentObject[0][0], minute, day)
		elif(day and not(minute)):
			print "<b>Tidak diketahui</b>"
		if(not(output) or output==['']):
			print "<b>Tidak diketahui</b>"
		else:
			print "Ruangan Mata Kuliah yang diikuti oleh <b>"+studentObject[0][1].title()+"</b> ["+studentObject[0][0].upper()+"] di <b>", ", ".join(output),"</b>"
	elif(choosen == 3):
		import allSchedule
		if(str(day) == '0'):
			print "<b>Jadwal kosong, tidak ada kegiatan kampus</b>"
		elif(not(day)):
			output, status = allSchedule.show(studentObject[0][0])
			if(status):
				print "Berikut jadwal <b>"+studentObject[0][1].title()+"</b> ["+studentObject[0][0].upper()+"] :<br/>"
			print output
		elif(day!=0):
			output, status = allSchedule.show(studentObject[0][0], day)
			if(status):
				print "Berikut jadwal <b>"+studentObject[0][1].title()+"</b> ["+studentObject[0][0].upper()+"] di hari <b>"+days[str(day)]+"</b>:<br/>"
			print output
	
	elif(choosen == 4):
		import allMatkul
		print "berikut seluruh mata kuliah yang diambil oleh <b>"+studentObject[0][1].title()+"</b> ["+studentObject[0][0].upper()+"] : <br/><div class='left-align nim-table'>"
		print allMatkul.show(studentObject[0][0])+"</div>"
	elif(choosen == 5):
		import bulkSpareTime
		output = bulkSpareTime.lookup(studentObject[0][0])
		print "Berikut seluruh jadwal kosong <b>"+studentObject[0][1].title()+"</b> ["+studentObject[0][0].upper()+"] :"
		print output

elif(studentCount == 0 and mkCount == 1):
	# 2, 3, 5, 11, 12
	qweight = [0,0,0,0,0]
	weight = [["kapan", [0.2,0,0.8,0,0]],["bisa", [0.4,0,0.6,0,0]],["dapat", [0.3,0,0.7,0,0]],["jadwal", [0.1,0.1,0.8,0,0]],["ulang", [0.1,0,0.9,0,0]],["kembali", [0.1,0,0.9,0,0]],["syarat", [1,0,0,0,0]],["mana", [0,0.7,0,0.3,0]],["ruang", [0,1,0,0,0]],["tempat", [0,1,0,0,0]],["lokasi", [0,1,0,0,0]],["siapa", [0,0,-1,1,-2]],["aja", [0.4,0,0,0.6,0]],["ikut", [0,0,0,1,1]],["siswa", [0,0,0,1,1]],["ambil", [0,0,0,1,1]],["jumlah", [-1,-1,-1,-1,3]],["berapa", [-1,-1,-1,-1,3]],["apa", [0.5,0,0.1,0.4,0]]]
	for word in correctedQuery.split(' '):
		for w in weight:
			if w[0] in word:
				for i in range(5):
					qweight[i] = qweight[i] + w[1][i]
				break 
	print "<!--"+str(qweight)+"-->"
	choosen = qweight.index(max(qweight)) + 1
	if(choosen == 1):
		import prasyaratSearch
		print prasyaratSearch.search(mkObject[0][0], mkObject[0][1])
	elif(choosen == 2):
		import locateMatkul
		output, status = locateMatkul.search(mkObject[0][0], False, minute, day)
		if(not(output) or output==['']):
			print "<b>Tidak diketahui</b>"
		else:
			print "Ruangan Mata Kuliah <b>"+mkObject[0][1]+"</b> di <b>", ", ".join(output),"</b>"
	elif(choosen == 3):
		import reschedule
		print "Berikut waktu untuk penjadwalan ulang mata kuliah <b>" + mkCorrect[1] + "</b>"
		print reschedule.this(mkObject[0][0])
	elif(choosen == 4):
		import matkulParticipant
		print "Berikut daftar mahasiswa yang mengambil mata kuliah <b>"+mkObject[0][1]+"</b> : <br/><div class='left-align nim-table'>"
		print matkulParticipant.lookup(mkObject[0][0])+'</div>'
	elif(choosen == 5):
		import countStudent
		output = countStudent.count(mkObject[0][0])
		print "Jumlah mahasiswa yang mengambil mata kuliah <b>"+mkObject[0][1]+"</b> : <h1>"+str(output)+"</h1>"
elif(studentCount == 1 and mkCount == 1):
	# 3, 6
	qweight = [0,0]
	weight = [["mana", [0.9,0.1]],["ruang", [0.9,0.1]],["dalam", [0.8,0.2]],["ada", [0.9,0.1]],["ikut", [0.4,0.6]],["oleh", [0.3,0.7]],["tempat", [0.9,0.1]],["lokasi", [0.9,0.1]],["apa", [0.1,0.9]],["ambil", [0.1,0.9]],["ilih", [0.2,0.8]]]
	for word in correctedQuery.split(' '):
		for w in weight:
			if w[0] in word:
				for i in range(2):
					qweight[i] = qweight[i] + w[1][i]
				break 
	print "<!--"+str(qweight)+"-->"
	choosen = qweight.index(max(qweight)) + 1
	if(choosen == 1):
		import locateMatkul
		output, status = locateMatkul.search(mkObject[0][0], studentObject[0][0], minute, day)
		if(not(output) or output==['']):
			print "<b>Tidak diketahui</b>"
		elif(status):
			print "Ruangan Mata Kuliah <b>"+mkObject[0][1]+"</b> yang diikuti oleh <b>"+studentObject[0][1].title()+"</b> ["+studentObject[0][0].upper()+"] di <b>", ", ".join(output),"</b>"
		else:
			print "Sepertinya <b>"+studentObject[0][1].title()+"</b> ["+studentObject[0][0].upper()+"] tidak mengambil mata kuliah <b>"+mkObject[0][1]+"</b>, berikut ruangan yang dipakai mata kuliah tersebut <b>", ", ".join(output), "</b>"
	elif(choosen == 2):
		import isTake
		status = isTake.take(studentObject[0][0],  mkObject[0][0])
		if(status):
			print "yap, <b>"+studentObject[0][1].title()+"</b> ["+studentObject[0][0].upper()+"] mengambil mata kuliah <b>"+mkObject[0][1]+"</b>."
		else:
			print "tidak, <b>"+studentObject[0][1].title()+"</b> ["+studentObject[0][0].upper()+"] tidak mengambil mata kuliah <b>"+mkObject[0][1]+"</b>."
elif(studentCount == 2):
	# 9
	import commonClass
	dataCommon = commonClass.search(studentObject[0][0], studentObject[1][0])
	if(not(dataCommon)):
		print "<b>&#60;tidak ditemukan&#62;</b><br/>tidak ditemukan jadwal bersama antara <b>"+studentObject[0][1]+"</b> dan <b>"+studentObject[1][1]+"</b>."
	else:
		print "Berikut jadwal bersama antara <b>"+studentObject[0][1].title()+"</b> ["+studentObject[0][0].upper()+"] dan <b>"+studentObject[1][1].title()+"</b> ["+studentObject[1][0].upper()+"] :<br/>"
		print dataCommon
else:	
	printerror()
	sys.exit()
	
stop = default_timer()
print '<div id="time_exec">(<b>'+str(stop-start)+'</b>) detik'

e = open('_latest_query_.txt', 'a')
e.write(query+"\n")
e.close()

f = open('count.txt', 'r')
count = f.read()
count = int(count) + 1
f.close()

g = open('count.txt', 'w')
g.write(str(count))
g.close()

"""
v # 1 - Mengetahui <nama> kosong atau tidak pada <waktu> || spareTime.py
v # 2 - Mengetahui prasyarat dari <matkul> || prasyaratSearch.py
v # 3 - Mengetahui ruangan <matkul> dengan <nama> pada <waktu> || locateMatkul.py
v # 4 - Mengetahui lokasi <nama> pada <waktu> || locateMatkul.py
v # 5 - Mengetahui jadwal pengganti <matkul>
v # 6 - Mengetahui <nama> mengambil <matkul> || isTake.py
v # 7 - Mengetahui seluruh jadwal dari <nama>  pada <hari>  || allSchedule.py
v # 8 - Mengetahui semua matkul yang diambil <nama> || allMatkul.py 
v # 9 - Mengetahui waktu <nama1> dan <nama2> dalam satu ruangan || commonClass.py
v # 10 - Mengetahui jadwal kosong <nama> pada <waktu> 
v # 11 - Mengetahui siapa saja yang mengambil matkul || classTaken.py
v # 12 - Mengetahui jumlah mahasiswa yang mengambil matkul || countStudent.py 
"""