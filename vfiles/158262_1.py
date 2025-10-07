n = int(input("Enter any year that is to be chacked for leap year:"))
if (n%4==0 and n%100!=0) or (n%400==0):
   print("The given year is a leap year")
else:
   print("It is not a leap year")