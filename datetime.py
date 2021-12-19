import datetime
import pytz
today=datetime.date.today()
print(today)
birthday=datetime.date(2002,2,23)
print(birthday)
#finding days since birthday
days_since_birth=(today-birthday).days
print(days_since_birth)
#time delattr
#adding 10 days to the date 
time_delta=datetime.timedelta(days=5)
#adding 12 hrs to time
hour_delta=datetime.timedelta(hours=12)
print(datetime.datetime.now()+hour_delta)
print(today+time_delta)
print(today-time_delta)

print(today.day)
#returns time structure of today
print(today.timetuple())

print(today.weekday())
print(datetime.time(12,52,56,45))

#datetime.date(yyyy,m,dd)
#datetime.time(h,m,s,ms)
#datetime.datetime(yyyy,m,dd,h,m,s,ms)
#for finding out day and time of current -datetime.datetime.now()
#for finfding or printing todyas date-datetime.date(yy,m,dd)
#for just finding todays date-datetime.date.today()

#time zone
#tz=timezone,pytz=python contained time zone.utc
datetime_today=datetime.datetime.now(tz=pytz.UTC)
print(datetime_today) 
#datetime.astimezone(pytz.timezone(''))
dattime_pacific=datetime_today.astimezone(pytz.timezone('US/pacific'))
print(dattime_pacific)
#for tz in pytz.all_timezones:
 # print(tz)
#string formating with dates
#2021-12-12-(input)>march 09,2019
#strftime(=formatting)
print(dattime_pacific.strftime('%B %d %y'))
#b-month
#d-date
#y-year
#strptime(p=parsing i.e, joining)
date_1=datetime.datetime.strptime('March 12,2021','%B %d, %y')
print(date_1)
