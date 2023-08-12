import datetime
date1 = datetime.datetime(2023, 7, 26)
date2 = datetime.datetime(2023, 8, 15)
if date1 < date2:
    print("date1 is before date2")
elif date1 > date2:
    print("date1 is after date2")
else:
    print("date1 and date2 are the same")

if date1.date() < date2.date():
    print("date1 is before date2")
elif date1.date() > date2.date():
    print("date1 is after date2")
else:
    print("date1 and date2 are the same date")
