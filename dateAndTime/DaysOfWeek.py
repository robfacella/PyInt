# Python program to get the day of week of today or given date.
import datetime

#Determines Day of the Week for a date passed to it.
#Print message is arbitrary, but this type of code could be used for regular task scheduling.
def isWeekend(theDay):
    if theDay.weekday() > 4 :
        print ('It\'s a  weekend!')
    elif theDay.weekday() == 4 :
        print ('Thank Py it\'s Friday!')
    else:
        print ('It\'s a weekday, back to work.')

#For strftime formatting table see:
#http://www.cplusplus.com/reference/ctime/strftime/
dayofweek = datetime.date(1996, 6, 17).strftime("%A")
print(dayofweek)
# weekday Monday is 0 and Sunday is 6
print("weekday():", datetime.date(1996, 6, 17).weekday())
# isoweekday() Monday is 1 and Sunday is 7
print("isoweekday():", datetime.date(1996, 6, 17).isoweekday())
print(' ')

dayofweek = datetime.datetime.today().strftime("%A")
print(dayofweek)
print("weekday():", datetime.datetime.today().weekday())
print("isoweekday():", datetime.datetime.today().isoweekday())

print(' ')
thisDay = datetime.datetime.today()
isWeekend(thisDay)
