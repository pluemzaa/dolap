A=input("Enter any year that is to be checked for leap year:")
A=int(A)
if (A%4==0) and (A%100!=0) or (A%400==0):
  print("The given year is a leap yea")
else :
  print("It is not a leap year")