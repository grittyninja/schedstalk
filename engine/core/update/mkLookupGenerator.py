from time import sleep 
import sys 
import timeit
start = timeit.default_timer()
print "\n\n::: Generate mkLookup to increase performance :::\n"
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
import mkList
data = mkList.matkuls
for mk in data:
    visited += 1
    progress = round(visited/float(len(data))*100,2)
    sys.stdout.write('\r')
    sys.stdout.write("[%-100s] %.2f%%" % ('='*int(progress), progress))
    sys.stdout.flush()
    lookup[mk[0]] = mk[1]

file = open("mkLookup.py", 'w')
file.write("lookup = ")
file.write(str(lookup))
file.close()

stop = timeit.default_timer()
print "\n\nWaktu eksekusi :", 
print_waktu(str(stop - start))