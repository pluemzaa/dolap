num=input("Enter any year that is to be checked for leap year:",)
num=int(num)
if num%4==0:
    if num%100 !=0:
        print("The given year is a leap year")
if a%400==0:
    print("The given year is a leap year")
else:
    print("it is not a leap year")