a = int(input("Enter any year that is to be checked for leap year:"))
if a%4:
    print("The given year is a leap year")
elif a%400:
    print("The given year is a leap year")
elif a%100:
    print("It is not a leap year")