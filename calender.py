import calendar
yy=2017
mm=2
dd=23
print(calendar.month(yy,mm))
print(calendar.weekheader(3))
#print(calendar.calendar(yy,1,2,5))
print(calendar.firstweekday())
#it show the calender in matrix format
print(calendar.monthcalendar(yy,mm))
#boolean statement
leapyear=calendar.isleap(2020)
print(leapyear)
#to cslculate no of leap years in a range
range_of_leapyears=calendar.leapdays(2000,2008)
print(range_of_leapyears)
print(calendar.weekday(2021,2,23))
