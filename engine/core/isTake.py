#!/usr/bin/python

def take(nim, matkul):
    import attendClassLookup
    import matkulClassLookup
    nimClass = attendClassLookup.lookup[nim]
    matkulClass = matkulClassLookup.lookup[matkul]
    take = False
    for clas in matkulClass:
        for clas_ in nimClass:
            if clas == clas_:
                return True
    return False