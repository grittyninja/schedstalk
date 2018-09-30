#!/usr/bin/python

def show(nim, day=False):
    import attendClassLookup
    import classLookup
    import mkLookup
    days = {"0":"Tidak diketahui","1":"Senin","2":"Selasa","3":"Rabu","4":"Kamis","5":"Jumat","6":"Sabtu"}
    classes = attendClassLookup.lookup[nim]
    schedule = []
    if(not(day)):
        for clas in classes:
            temp = classLookup.lookup[clas]
            temp.append(clas)
            schedule.append(temp)
        if(len(schedule)==0):
            return "<b>Jadwal kosong, tidak ada kegiatan kampus</b>", 0
        head = '<table class="striped matkul-table"><thead><tr><th>Mata Kuliah</th><th>Ruangan</th><th>Hari</th><th>Waktu</th></tr></thead><tbody>'
        body = ''
        for sched in schedule:
            body += '<tr>'
            # matkul
            body += '<td>'+mkLookup.lookup[sched[0]].title()+' ('+sched[5][0]+')</td>'
            # ruangan
            if(sched[1]==""):
                sched[1] = "Tidak diketahui"
            body += '<td>'+sched[1]+'</td>'
            # hari 
            body += '<td>'+days[sched[2]]+'</td>'
            # waktu 
            body += '<td>'+sched[3]+'-'+sched[4]+'</td>'
            body += '</tr>'
        foot = '</tbody></table>'
        return head+body+foot, 1
        
    else:
        for clas in classes:
            dayClass = classLookup.lookup[clas][2]
            if(int(dayClass) == int(day)):
                temp = classLookup.lookup[clas]
                temp.append(clas)
                schedule.append(temp)
        if(len(schedule)==0):
            return "<b>Jadwal kosong, tidak ada kegiatan kampus</b>", 0
        head = '<table class="striped matkul-table"><thead><tr><th>Mata Kuliah</th><th>Ruangan</th><th>Waktu</th></tr></thead><tbody>'
        body = ''
        for sched in schedule:
            body += '<tr>'
            # matkul
            body += '<td>'+mkLookup.lookup[sched[0]].title()+' ('+sched[5][0]+')</td>'
            # ruangan 
            if(sched[1]==""):
                sched[1] = "Tidak diketahui"
            body += '<td>'+sched[1]+'</td>'
            # waktu 
            body += '<td>'+sched[3]+'-'+sched[4]+'</td>'
            body += '</tr>'
        foot = '</tbody></table>'
        return head+body+foot, 2
