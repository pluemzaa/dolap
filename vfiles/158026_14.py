a = int(input("Enter any year that is to be checked for leap year: "))
if a%4:
  a=a%100
  a=a%400
  print("The given year is a leap year")
else :
  print("It is not a leap year")