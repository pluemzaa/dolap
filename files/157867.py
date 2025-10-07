A = int(input("Enter any year that is to be checked for leap year:"))
if A%4 ==0 and A%100 !=0:
  print("The given year is a leap year")
elif A%400 ==0:
   print("The given year is a leap year")
else:
    print("It is not a leap year")