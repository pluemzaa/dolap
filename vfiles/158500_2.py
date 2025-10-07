yr=int(input("Enter any year that is to be checked for leap year:"))
if yr%100!=0 and yr%4==0 or yr%400==0:
    print("The given year is a leap year")
else:
    print("It is not a leap year")