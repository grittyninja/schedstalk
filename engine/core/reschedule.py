import sys
sys.path.append('data')
import matkulPartLookup
import attendClassLookup
import classLookup
import matkulClassLookup

days = {'0':'Minggu','1':'Senin','2':'Selasa','3':'Rabu','4':'Kamis','5':'Jumat','6':'Sabtu'}
def getTime(minute):
	hour = minute // 60
	minute = minute % 60
	minute = "%02d" % (minute,)
	return str(hour)+":"+str(minute)

def timeFormat(data_):
    schedule = []
    for data in data_:
        day = []
        data.sort()
        for i in range(len(data)//2):
            start = data[i*2]*10 + 420
            end = data[i*2+1]*10 + 420
            day.append(getTime(start)+"-"+getTime(end))
        schedule.append(day)
    return schedule

def cssFormat(data):
    head = '<table class="striped matkul-table"><tbody>'
    body = ''
    i = 1
    for dat in data:
        day = days[str(i)]
        body += "<tr><td><b>"+day+"</b></td></tr>"
        for da in dat:
            body += "<tr><td>"+da+"</td></tr>"
        i += 1            
    foot = '</tbody></table>'
    return head+body+foot

def this(matkul):
    listStudent = matkulPartLookup.lookup[matkul]
    listClass = []

    spareSequence = [
        ['1','0000000000000000000000000000000000000000000000000000000000000000'],
        ['2','0000000000000000000000000000000000000000000000000000000000000000'],
        ['3','0000000000000000000000000000000000000000000000000000000000000000'],
        ['4','0000000000000000000000000000000000000000000000000000000000000000'],
        ['5','0000000000000000000000000000000000000000000000000000000000000000']
        ]
    for student in listStudent:
        listClass.extend(attendClassLookup.lookup[student])
    listClass = list(set(listClass))
    for clas in listClass:
        data = classLookup.lookup[clas]
        if(int(data[2])<6 and int(data[2])>0):
            startTime = data[3].split('.')
            endTime = data[4].split('.')
            startTime = (int(startTime[0])*60 + int(startTime[1])-420) // 10
            endTime = (int(endTime[0])*60 + int(endTime[1])-420) // 10
            if(endTime>63):
                endTime = 63
            for i in range(endTime-startTime):
                listSched = list(spareSequence[int(data[2])-1][1])
                listSched[i+startTime] = '1'
                spareSequence[int(data[2])-1][1] = ''.join(listSched)
    bulkSchedule = []
    for i in range(1,6):
        day = i
        sequence = spareSequence[day-1][1]
        schedule = []
        start = False
        end = False
        for i in range(len(sequence)):
            if(sequence[i]=='0' and i==0):
                start = True
                end = False
                schedule.append(i)
            elif(sequence[i]=='0' and i==len(sequence)-1):
                end = True
                start = False
                schedule.append(i+1)
            elif(sequence[i]=='0' and sequence[i-1]=='1' and not(start)):
                start = True
                end = False
                schedule.append(i)
            elif(sequence[i]=='0' and sequence[i+1]=='1' and not(end)):
                start = False
                end = True
                schedule.append(i+1)
        bulkSchedule.append(schedule)
    return cssFormat(timeFormat(bulkSchedule))

    