#!/usr/bin/python

import matkulPartLookup
def count(matkul):
    listParticipant = matkulPartLookup.lookup[matkul]
    return len(listParticipant)