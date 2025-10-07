year=int(input("Enter any year that is to be checked for leap year: "))
if a%400==0:
  print("The given year is a leap year")
elif a%4==0:
  a=a%100
  print("The given year is a leap year")
else :
  print("It is not a leap year")