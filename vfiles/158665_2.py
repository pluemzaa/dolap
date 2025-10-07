Y=int(input('Enter any year that is to be checked for leap year:'))
a=Y%4
b=Y%100
c=Y%400
if (a==0 and b!=0)or c==0:
    print("The given year is a leap year")
else:
    print("It is not a leap year")