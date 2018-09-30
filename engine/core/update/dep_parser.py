#!/usr/bin/python
import urllib2 as ulib
from bs4 import BeautifulSoup as bsoup 
import timeit
start = timeit.default_timer()
from time import sleep 
import sys 



print "::: Get All Departements :::\n"
# get html source 
html = ulib.urlopen("http://krs.ipb.ac.id/krs/jadwaldep?dep=G6")

# initiate parser
soup = bsoup(html, 'html.parser')

# define null list
parsed_jurusan = []
value = soup.find_all('option',{'value':True})
   
for m in value:
	parsed_jurusan.append(str(m['value']))

del parsed_jurusan[0] # delete null

# pop four last list
parsed_jurusan = parsed_jurusan[:-4]
 
sys.stdout.write('\r')
sys.stdout.write("[%-100s] %d%%" % ('='*100, 5*20))
sys.stdout.flush()

# write
file = open("deplist.py", 'w')
file.write("departements = ")
file.write(str(parsed_jurusan))
file.close()
stop = timeit.default_timer()
print "\n\nWaktu eksekusi : " + str(stop - start) + " detik"
