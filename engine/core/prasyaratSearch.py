#!/usr/bin/python
def cssFormat(array, nama):
    head = "<b>Prasyarat mata kuliah "+nama+" : </b>"
    if(len(array)==0):
        return head+"<b>&#60;tidak ada&#62;</b>"
    else:
        dataCSSList = "<ul>"
        for mk in array:
            mk = mk.split(' ')
            kode = mk[0]
            mk.pop(0)
            mk = " ".join(mk)
            mk = mk.title()
            mk = mk[1:-1]
            mk += " ["+kode.upper()+"]"
            mk.replace(kode,"")
            dataCSSList += "<li> - "+mk+"</li>"
        dataCSSList += "</ul>"
        return head+dataCSSList
        
def search(kodeMatkul, namaMatkul):
    import mkList
    matkuls = mkList.matkuls
    for matkul in matkuls:
        if matkul[0] == kodeMatkul:
            return cssFormat(matkul[2], namaMatkul)
            break 