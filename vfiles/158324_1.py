y = input("Enter any year that is to be checked for leap year: ")
y = int(y)
if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
    print("The given year is a leap year")
else:
    print("It is not a leap year")