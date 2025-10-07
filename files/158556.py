leap = int(input("Enter any year that is to be checked for leap year:"))
if leap%4 == 0 and leap%100 != 0:
  print("The given year is a leap year")
elif leap%400 == 0:
  print("The given year is a leap year")
else:
  print("It is not a leap year")