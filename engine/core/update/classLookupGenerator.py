#!/usr/bin/python
from time import sleep 
import sys 
import timeit
start = timeit.default_timer()
print "\n\n::: Generate classLookup to increase performance :::\n"
def print_waktu(waktu):
	waktu = float(waktu)
	menit = int(waktu // 60)
	detik = waktu % 60
	if(menit>0):
		print str(menit) + " menit",
	if(detik>0):
		print str(detik) + " detik"
visited = 0
lookup = {}
import scheduleData
data = scheduleData.data
for matkul in data:
    visited += 1
    progress = round(visited/float(len(data))*100,2)
    sys.stdout.write('\r')
    sys.stdout.write("[%-100s] %.2f%%" % ('='*int(progress), progress))
    sys.stdout.flush()
    days = matkul[1]
    for day in days:
		for sched in day[1]:
		    lookup[sched[0]] = [matkul[0],sched[1],day[0],sched[2],sched[3]]

file = open("classLookup.py", 'w')
file.write("lookup = ")
file.write(str(lookup))
file.close()

stop = timeit.default_timer()
print "\n\nWaktu eksekusi :", 
print_waktu(str(stop - start))