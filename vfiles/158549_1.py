num = int(input("Enter your number"))
if num%4==0 and num%100!=0 and num%400==0:
 print("The given year is a leap year")
else :
 print("It is not a leap year")