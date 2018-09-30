#!/usr/bin/python
import sys
sys.path.append('data')
def cssFormat(array, clas):
    activity = {'P':'Praktikum', 'K':'Kuliah', 'R':'Responsi'}
    activity = activity[clas[0]]
    import mkLookup
    mk = mkLookup.lookup[array[0]]
    html = "ada <b>"+activity+"</b> mata kuliah <b>"+mk.title()+"</b> pada pukul <b>"+array[3]+"</b> sampai <b>"+array[4]+"</b>"
    if(array[1] != ''):
        html += ' di ruang <b>'+array[1]+'</b>'
    return html

def search(nim, day , minute):
    day = int(day)
    minute = int(minute)
    # get all nim classes
    import attendClassLookup
    import classLookup
    kosong = True
    classes = attendClassLookup.lookup[nim]
    for clas in classes:
        data = classLookup.lookup[clas]
        if(int(data[2]) == day):
            startTime = data[3].split('.')
            endTime = data[4].split('.')
            startTime = int(startTime[0])*60 + int(startTime[1])
            endTime = int(endTime[0])*60 + int(endTime[1])
            if(minute <= (endTime+5) and minute >= (startTime-5)):
                kosong = False
                return cssFormat(data, clas), kosong
    if(kosong):
        return False, kosong