#!/usr/bin/python

def cssFormat(array):
    body = ""
    array.sort()
    import studentLookup
    for nim in array:
        studentName = studentLookup.lookup[nim]
        body += "<li>- <b>"+studentName.title()+"</b> ["+nim.upper()+"]</li>"
    return "<ul>"+body+"</ul>"
    
def lookup(matkul):
    import matkulPartLookup
    participants = matkulPartLookup.lookup[matkul]
    return cssFormat(participants)
    