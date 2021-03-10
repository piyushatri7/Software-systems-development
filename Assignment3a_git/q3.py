import json

f1 = open("Employee1.txt", "r")
f2 = open("Employee2.txt", "r")

input1 = f1.read().replace("'", "\"")
input2 = f2.read().replace("'", "\"")   

f1.close()
f2.close()

dic1 = json.loads(input1)
dic2 = json.loads(input2)


name1 = str(list(dic1.keys())[0])
name2 = str(list(dic2.keys())[0])

#store only date and slots
dic1 = dic1[name1]
dic2 = dic2[name2]

#store dates
date1 = str(list(dic1.keys())[0]) 
date2 = str(list(dic2.keys())[0])

#store the working time slots
slots1 = []
slots2 = []

#save interavals as list of 2 elements
for interval in dic1[date1]:
    slots1.append(list(interval.split('-')))

for interval in dic2[date2]:
    slots2.append(list(interval.split('-')))

tempslot1 = []
tempslot2 = []

#convert employee1 slots to minutes
for interval in slots1:
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

    tempslot1.append([minutes1,minutes2])

#convert employee2 slots to minutes
for interval in slots2:
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
    
    tempslot2.append([minutes1,minutes2])

slots1 = tempslot1.copy()
slots2 = tempslot2.copy()
#print(slots1)
#print(slots2)

#reduce to merge interval problem
mslots = []
mslots = tempslot1.copy()
for x in tempslot2:
    mslots.append(x.copy())
    
mslots.sort()

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
#print(freeslots)

#print(slots1) 
#print(findFreeSlots(slots1))

#print(slots2)
#print(findFreeSlots(slots2))

############################
#function to format slots in output format, input is list of list
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

#print(slots1)
#print((findFreeSlots(slots1)))
#print(formatSlots(findFreeSlots(slots1)))

#print(slots2)
#print((findFreeSlots(slots2)))
#print(formatSlots(findFreeSlots(slots2)))


f = open("output.txt", "w")
f.write("Available slot\n")
f.write( name1 + " "  +  str(formatSlots(findFreeSlots(slots1))) + "\n" )
f.write( name2 + " "   +  str(formatSlots(findFreeSlots(slots2))) + "\n\n")        
f.write("Slot Duration: " + str(duration/60) + " hour\n")
if availslot != []:
                            #make availslot a list of list  
    op = {date1:formatSlots([availslot])}
    f.write(str(op))
else:
    f.write("no slot available")
f.close()
