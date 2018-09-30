from time import sleep 
import sys 
import timeit
start = timeit.default_timer()
print "\n\n::: Generate attendClassLookup to increase performance :::\n"
def print_waktu(waktu):
	waktu = float(waktu)
	menit = int(waktu // 60)
	detik = waktu % 60
	if(menit>0):
		print str(menit) + " menit",
	if(detik>0):
		print str(detik) + " detik"
visited = 0
import studentList
import scheduleData
studentList = studentList.students
lookup = {}

for student in studentList:
    student = student[0]
    visited += 1
    progress = round(visited/float(len(studentList))*100,2)
    sys.stdout.write('\r')
    sys.stdout.write("[%-100s] %.2f%%" % ('='*int(progress), progress))
    sys.stdout.flush()
    
    classList = []
    for matkul in scheduleData.data:
        days = matkul[1]
        for day in days:
    	    for sched in day[1]:
    	        nims = sched[4]
    	        if student in nims:
    	            classList.append(sched[0])
    lookup[student] = classList

file = open("attendClassLookup.py", 'w')
file.write("lookup = ")
file.write(str(lookup))
file.close()

stop = timeit.default_timer()
print "\n\nWaktu eksekusi :", 
print_waktu(str(stop - start))