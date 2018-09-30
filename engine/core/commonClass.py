#!/usr/bin/python

def cssFormat(array):
    head = '<table class="striped matkul-table"><thead><tr><th>Mata Kuliah</th><th>Ruangan</th><th>Hari</th><th>Waktu</th></tr></thead><tbody>'
    body = ''
    for sched in array:
        body += '<tr>'
        for sch in sched:
            body += '<td>'+sch+'</td>'
        body += '</tr>'
    foot = '</tbody></table>'
    return head+body+foot
    
def correctDataCommon(data):
    day = {"0":"Tidak diketahui","1":"Senin","2":"Selasa","3":"Rabu","4":"Kamis","5":"Jum'at","6":"Sabtu"}
    newdata = []
    import mkLookup
    for schedule in data:
        temp = mkLookup.lookup[schedule[0]].title()
        temp += " ("+schedule[5][0]+")"
        schedule[0] = temp
        schedule[2] = day[schedule[2]]
        schedule[3] += " - "+schedule[4]
        schedule = schedule[:-2]
        newdata.append(schedule)
    return newdata
        
def search(nim1, nim2):
    dataCommon = []
    import attendClassLookup
    commonClass1 = attendClassLookup.lookup[nim1]
    commonClass2 = attendClassLookup.lookup[nim2]
    commonClass = list(set(commonClass1) & set(commonClass2))
    
    if(len(commonClass)==0):
        return False
        
    import classLookup
    for clas in commonClass:
        temp = classLookup.lookup[clas]
        if(temp[1]==""):
            temp[1] = "Tidak diketahui"
        dataCommon.append([temp[0], temp[1], temp[2], temp[3], temp[4], clas])
    return cssFormat(correctDataCommon(dataCommon))
    
    