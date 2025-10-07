year = input("Enter any year that is to be checked for leap year:")
year = int(year)
if  year % 400 == 0:
    print("The given year is a leap year")
elif year % 100 == 0:
    print("It is not a leap year")
elif year % 4 == 0:
    print("The given year is a leap year")
else :
    print("It is not a leap year")