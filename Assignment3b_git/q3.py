import json
import os

from os import listdir
from os.path import isfile, join
filenames = [f for f in listdir("Emp_files") if isfile(join("Emp_files", f))]
#print(filenames)

dirname = next(os.walk('.'))[1]
dirname = dirname[0]

mslots = []
busyslotlist = []
namelist = []
datecheck = {}

for file in filenames:
    f = open((dirname + "/" + file) , "r")

    inp = f.read().replace("'", "\"")     #replace single quotes by double

    f.close()

    dic = json.loads(inp)

    name = str(list(dic.keys())[0])
    namelist.append(name)
    
    #store only date and slots
    dic = dic[name]

    #store date
    date = str(list(dic.keys())[0])
    datecheck[date] = 1

    #store the working time slots
    slots = []

    #save interavals as list of 2 elements
    for interval in dic[date]:
        slots.append(list(interval.split('-')))

    #print(slots)   #prints only timeslots of employees
    
    tempslot = []

    #convert employee slots to minutes
    for interval in slots:
        st = interval[0].strip()
        ed = interval[1].strip()

        minutes1 = 0
        minutes2 = 0

        #convert start time to minutes
        if(st.find("AM") != -1):
            st = st.replace("AM","")
            time = st.split(":")
            minutes1 = int(time[0])%12 * 60 + int(time[1])
            
        elif(st.find("PM") != -1):
            st = st.replace("PM","")
            time = st.split(":")
            minutes1 = int(time[0])%12 * 60 + int(time[1]) + 12*60

        #convert end time to minutes
        if(ed.find("AM") != -1):
            ed = ed.replace("AM","")
            time = ed.split(":")
            minutes2 = int(time[0])%12 * 60 + int(time[1])
            
        elif(ed.find("PM") != -1):
            ed = ed.replace("PM","")
            time = ed.split(":")
            minutes2 = int(time[0])%12 * 60 + int(time[1]) + 12*60

        tempslot.append([minutes1,minutes2])

    slots = tempslot.copy()
    #print()
    #print(slots)        #slot times converted to minutes
    temp = slots.copy()
    busyslotlist.append(temp)
    
    #reduce to merge interval problem by storing all slots in one list
    for x in tempslot:
        mslots.append(x.copy())
    #Here I am sorting after each iteration    
    mslots.sort()

#print()
#print(busyslotlist)

#print()
#print(mslots)

#merge intervals algo
merged = []
temp = mslots[0].copy()
merged.append(temp)
i=1
j=0
while(i < len(mslots)):
    if( merged[j][1] < mslots[i][0]):
        temp = mslots[i].copy()
        merged.append(temp)
        j=j+1
    else:
        merged[j][1] = max(mslots[i][1] , merged[j][1])
        
    i=i+1

#print()    
#print(merged)



############################
#Function to find free slots
def findFreeSlots(intervals):
    frees = []
    if 540 < intervals[0][0]:
        frees.append([540,intervals[0][0]])

    for i in range(len(intervals)-1):
        if(intervals[i][1] != intervals[i+1][0]):
            frees.append([intervals[i][1] , intervals[i+1][0]])

    if intervals[len(intervals)-1][1] < 1020:
        frees.append([intervals[len(intervals)-1][1],1020])
        
    return (frees)
############################

freeslots = findFreeSlots(merged)
#print()
#print(freeslots)

#print(slots1) 
#print(findFreeSlots(slots1))

#print(slots2)
#print(findFreeSlots(slots2))

############################
#function to format slots in output format, INPUT is list of list
def formatSlots(slots):
    formatted = []
    for time in slots:
        
        st = int(time[0])
        
        #formatting minutes to always have 2 digits
        if st%60 == 0:
            stmin = "00"
        else:
            stmin = str(st%60)
            
        #AM case
        if(st < 12*60):
           temp1 =  str(int(st/60)) + ":" + stmin + "AM"
        #PM case
        else:
            if(int((st/60)%12) == 0):
                temp1 = "12:" + stmin + "PM"
            else:
                temp1 =  str(int(st/60 - 12)) + ":" + stmin + "PM"

        
        ed = int(time[1])
        
        #formatting minutes to always have 2 digits
        if ed%60 == 0:
            edmin = "00"
        else:
            edmin = str(ed%60)
            
        #AM case
        if(ed < 12*60):
           temp2 =  str(int(ed/60)) + ":" + edmin + "AM"
        #PM case
        else:
            if(int((ed/60)%12) == 0):
                temp2 = "12:" + edmin + "PM"
            else:
                temp2 =  str(int(ed/60 - 12)) + ":" + edmin + "PM"
                
        formatted.append(temp1 + " - " + temp2)
    return formatted
############################

duration = float(input())*60

availslot = []
for free in freeslots:
    if((free[1]-free[0]) >= duration):
        availslot = [free[0] , int(free[0]+duration)]
        break
    
#print()
#print(formatSlots([availslot]))

#print(slots1)
#print((findFreeSlots(slots1)))
#print(formatSlots(findFreeSlots(slots1)))

#print(slots2)
#print((findFreeSlots(slots2)))
#print(formatSlots(findFreeSlots(slots2)))


f = open("output.txt", "w")
f.write("Available slot\n")
for i in range(len(busyslotlist)):
    f.write( namelist[i] + " "  +  str(formatSlots(findFreeSlots(busyslotlist[i]))) + "\n" )

f.write("Slot Duration: " + str(duration/60) + " hour\n")

#slot is available abd all dates are same
if availslot != [] and len(datecheck) == 1:
           #append date as key                     #make availslot a list of list  
    op = { list(datecheck.keys())[0] : formatSlots([availslot]) }
    f.write(str(op))
else:
    f.write("no slot available")
f.close()
