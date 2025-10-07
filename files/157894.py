y=int(input("Enter any year that is to be checked for leap year:"))
if y%4==0:
    print("The given year is a leap year")
elif y%400==0:
    print("The given year is a leap year")
else:
    print("It is not a leap year")