import calendar
cal=calendar.TextCalendar(calendar.SUNDAY)
str = cal.formatmonth(2019, 4)
print(str)

yr = int(input("Enter the Year"))
mnth = int(input("Enter the Month"))
print(calendar.month(yr, mnth))
