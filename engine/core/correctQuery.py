#!/usr/bin/python
from difflib import SequenceMatcher as SM
days = ["minggu","senin","selasa","rabu","kamis","jumat","sabtu"]
operasi_ = ["kurang", "lewat", "lebih"]
varMin = ["setengah","seperempat"]
corpus = "apa lagi berapa apakah saja lewat sajakah aku dapat tidak ini mata setengah seperempat kurang lebih menit satu sama mengambil bisa ulang kuliah sekarang saat matkul matakuliah sebutkan tersebut tampil tampilkan sebut mengapa kenapa kosong nganggur dijadwalkan jadwal kembali pada kan di ruang dimana kelas ruangan tempat jam siang malam sore pagi petang dosen mahasiswa dengan kapan kapankah waktu bertemu temu semua muncul munculkan hari senin selasa rabu kamis jumat sabtu minggu lokasi seluruh yang diambil ambil oleh diikuti ikut mengikuti dalam prasyarat syarat  atau dan"
listCorpus = corpus.split(" ")
# corpus 87 kata
def correct(query):
    hour = False
    minute = False
    newminute = False
    day = False
    operasi = False
    setengah = False
    newquery = ""
    query.replace("  "," ")
    qcorrect = query.split(" ")
    num = 0
    for qc in qcorrect:
        maxprob = 0
        qcCandidate = 0
        if(not(qc.isdigit())):
            for cor in listCorpus:
                prob = SM(None, qc, cor).ratio()
                if(prob > maxprob and prob > 0.7):
                    maxprob = prob
                    qcCandidate = cor
            if(maxprob!=0 and qcCandidate!=0):
                # check days
                if (qcCandidate in days) and not(day):
                    day = days.index(qcCandidate)
                # check operasi
                if (qcCandidate in operasi_) and not(operasi):
                    temp = operasi_.index(qcCandidate)
                    operasi = temp+1
                # check minute
                if (qcCandidate in varMin) and not(minute):
                    temp = varMin.index(qcCandidate)
                    if(temp == 0):
                        minute = 30
                        setengah = True
                    else:
                        minute = 15
    	        newquery += qcCandidate+" "
    	else:
    	    if(not(num)):
        	    qc = str(int(qc)%24)
        	    num += 1
        	    hour = int(qc)
        	    newquery += qc+" "
            elif(not(minute)):
                qc = int(qc)%60
                minute = qc 
    count = False
    if hour and (operasi or setengah):
        count = True
        if(operasi and setengah):
            if(operasi == 1):
                newminute = (hour * 60) - 30
            else:
                newminute = (hour * 60) + 30 
        elif(not(setengah)):
            if(operasi == 1):
                newminute = (hour * 60) - minute
            else:
                newminute = (hour * 60) + minute
        elif(not(operasi)):
            newminute = (hour * 60) - 30
    if(not(count) and hour):
        newminute = hour * 60
    if(newminute<360 and hour):
        newminute += 720
    return newquery[:-1], day, newminute