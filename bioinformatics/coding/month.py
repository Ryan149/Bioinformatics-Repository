name={}
name[0]="January"
name[1]="February"
name[2]="March"
name[3]="April"
name[4]="May"
name[5]="June"
name[6]="July"
name[7]="August"
name[8]="September"
name[9]="October"
name[10]="November"
name[11]="December"
def daysInMonth(month):
        days = 30
        if (month < 7):
                if (month % 2 == 0):
                        days = 31
                if (month == 1):
                        days = 28
        else:
                if (month % 2 == 1):
                        days = 31
        return days
daysInYear=0
for i in range(0,12):
 print "There are",daysInMonth(i),"days in",name[i]
 daysInYear=daysInYear+daysInMonth(i)
print "There are",daysInYear,"days in a non-leap year"
