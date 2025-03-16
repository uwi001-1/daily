#Find the date of the first Tuesday of a given month and year

from datetime import datetime, timedelta
def first_tuesday(month, year):
    for day in range(1,8):
        x = datetime(year,month,day)
        if x.strftime("%a") == "Tue":
            return x.date()   

month = int(input("Enter the month in number:  "))
year = int(input("Enter the year:  "))
print(first_tuesday(month,year))