year =int(input("Enter any year that is to be checked for leap year:"))
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("The given year is a leap year")
else:
    print("The given year is not a leap year")