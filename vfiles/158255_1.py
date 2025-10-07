years = int(input("Enter any year that is to be checked for leap year:"))
Y = years%4
if Y == 0:
    print("The given year is a leap year")
else:
    print("It is not a leap year")