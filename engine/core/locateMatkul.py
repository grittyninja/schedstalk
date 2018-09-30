
def search(matkul=False, nim=False, time=False, day=False):
    import matkulClassLookup
    import attendClassLookup
    import classLookup
    status = False
    if(matkul):
        listClass = matkulClassLookup.lookup[matkul]
    elif(not(matkul)):
        listClass = attendClassLookup.lookup[nim]
    if(nim and matkul):
        listStudentClass = attendClassLookup.lookup[nim]
        intersection = list(set(listClass) & set(listStudentClass))
        if(len(intersection)!=0):
            status = True
    if(status):
        listClass = intersection
    classroom = []
    if(not(time)):
        for clas in listClass:
            data = classLookup.lookup[clas]
            classroom.append(data[1])
    elif(time):
        for clas in listClass:
            data = classLookup.lookup[clas]
            if(day):
                if(int(data[2]) == int(day)):
                    startTime = data[3].split('.')
                    endTime = data[4].split('.')
                    startTime = int(startTime[0])*60 + int(startTime[1])
                    endTime = int(endTime[0])*60 + int(endTime[1])
                    if(time <= (endTime+5) and time >= (startTime-5) and clas[0]!='P'):
                        classroom.append(data[1])  
            else:
                startTime = data[3].split('.')
                endTime = data[4].split('.')
                startTime = int(startTime[0])*60 + int(startTime[1])
                endTime = int(endTime[0])*60 + int(endTime[1])
                if(time <= (endTime+5) and time >= (startTime-5) and clas[0]!='P'):
                    classroom.append(data[1]) 
    if(len(classroom)==0):
        return False, False
    return classroom, status
        
            
        