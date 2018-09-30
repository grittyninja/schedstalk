#!/usr/bin/python
def show(nim):
    matkul = []
    import attendClassLookup
    import classLookup
    nimClass = attendClassLookup.lookup[nim]
    for clas in nimClass:
        matkul.append(classLookup.lookup[clas][0])
    matkul = list(set(matkul))
    import mkLookup
    html = ""
    for mk in matkul:
        html += "<li>- "+mkLookup.lookup[mk].title() +" ["+mk.upper()+"] "+"</li>"
    return "<ul>"+html+"</ul>"