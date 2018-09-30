#!/usr/bin/python
from time import sleep 
import sys 
import timeit
start = timeit.default_timer()
print "\n\n::: Generate matkulPartLookup to increase performance :::\n"
def print_waktu(waktu):
	waktu = float(waktu)
	menit = int(waktu // 60)
	detik = waktu % 60
	if(menit>0):
		print str(menit) + " menit",
	if(detik>0):
		print str(detik) + " detik"
visited = 0
import scheduleData
matkuls = scheduleData.data
lookup = {}
for matkul in matkuls:
    visited += 1
    progress = round(visited/float(len(matkuls))*100,2)
    sys.stdout.write('\r')
    sys.stdout.write("[%-100s] %.2f%%" % ('='*int(progress), progress))
    sys.stdout.flush()
    participants = []
    days = matkul[1]
    for day in days:
		for sched in day[1]:
		    participants.extend(sched[4])
    participants = list(set(participants))
    lookup[matkul[0]] = participants

file = open("matkulPartLookup.py", 'w')
file.write("lookup = ")
file.write(str(lookup))
file.close()

stop = timeit.default_timer()
print "\n\nWaktu eksekusi :", 
print_waktu(str(stop - start))