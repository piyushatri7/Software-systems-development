import sys

f = open("date_calculator.txt", "r")

dt1 = f.readline().replace("Date1: ","")
dt2 = f.readline().replace("Date2: ","")
f.close()



def datesplit(date):
    if date.find('/') != -1:
        d1 = date.split('/')
    elif date.find('-') != -1:
        d1 = date.split('-')
    elif date.find('.') != -1:
        d1 = date.split('.')
    else:
        d1 = date.split(' ')

        #assigning number to monthname
        month_abbr = {'January,':1, 'Feburary,':2, 'March,':3, 'April,':4, 'May,':5, 'June,':6, 'July,':7,'August,':8, 'September,':9, 'October,':10, 'November,':11, 'December,':12,
                     'Jan,':1, 'Feb,':2, 'Mar,':3, 'Apr,':4, 'May,':5, 'Jun,':6, 'Jul,':7,'Aug,':8, 'Sep,':9, 'Oct,':10, 'Nov,':11, 'Dec,':12}
        d1[1] = month_abbr[d1[1]]

        #remove 1st,2nd,3rd,ith from day
        d1[0] = d1[0].replace('th', '');    d1[0] = d1[0].replace('st', '');    d1[0] = d1[0].replace('nd', '');    d1[0] = d1[0].replace('rd', '')
    return d1

d1 = datesplit(dt1)
d2 = datesplit(dt2)

#assign day,month according to input format
if len(sys.argv) == 2:
    dt_format = sys.argv[1]
    #print(len(sys.argv))
else:
    dt_format = "day_monthname_year"

if dt_format == "day_monthname_year" or (dt_format.find('/') != -1 and dt_format.split('/')[0] == 'dd') or (dt_format.find('-') != -1 and dt_format.split('-')[0] == 'dd') or (dt_format.find('.') != -1 and dt_format.split('.')[0] == 'dd'):       #dd/mm/yyyy and '10th sept, 2020' case
    #dd/mm/yy  or 1st January, 2020
    #days in current month
    day1 = int(d1[0])
    day2 = int(d2[0])
            
    #store month
    month1 = int(d1[1])
    month2 = int(d2[1])       

else:
    #mm/dd/yyyy case
    #days in current month
    day1 = int(d1[1])
    day2 = int(d2[1])
    
    #store month
    month1 = int(d1[0])
    month2 = int(d2[0])


#year will always be at the end
#store year
year1 = int(d1[2]) 
year2 = int(d2[2])


#from datetime import date 
#date1 = date(year1, month1, day1) 
#date2 = date(year2, month2, day2)

ty1 = year1
ty2 = year2

if month1 <= 2:
    ty1 -= 1
if month2 <= 2:
    ty2 -= 1
    
#number of leap years
leap1 = (int(ty1/4) + int(ty1/400) - int(ty1/100))
leap2 = (int(ty2/4) + int(ty2/400) - int(ty2/100))
#print(leap1)
#print(leap2)

#number of days till current year
day1 += 365*(year1-1) + leap1
day2 += 365*(year2-1) + leap2

monthday = [31,28,31,30,31,30,31,31,30,31,30,31]

#Add current month days
for i in range(0,month1 - 1):
    day1 += monthday[i]

for i in range(0,month2 - 1):
    day2 += monthday[i]

#print(abs(day1-day2))
#print((date2-date1).days , "days")


#print(str(abs(day1-day2)))
      
f = open("output.txt", "w")
f.write(str(abs(day1-day2)))
f.close()
