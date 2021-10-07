# Katie Beattie
# CS151, Dr. Rajeev
# October 6, 2021
# Programming Assignment 2
# Program Inputs: month and year that user enters
# Program Outputs: number of days in the month (including leap year cases)

monthStr = input("Enter a month: ")
month = int(monthStr)
yearStr = input("Enter a year: ")
year = int(yearStr)
if month == 1:
    mDays = 31
elif month == 2:
    if year % 4 == 0:
        year_isLeapYear = True
        mDays = 29
    else:
        year_isLeapYear = False
        mDays = 28
elif month == 3:
    mDays = 31
elif month == 4:
    mDays = 30
elif month == 5:
    mDays = 31
elif month == 6:
    mDays = 30
elif month == 7:
    mDays = 31
elif month == 8:
    mDays = 31
elif month == 9:
    mDays = 30
elif month == 10:
    mDays = 31
elif month == 11:
    mDays = 30
elif month == 12:
    mDays = 31
else:
    print("invalid month entry!")
print("There are ", mDays, " days in that month.")