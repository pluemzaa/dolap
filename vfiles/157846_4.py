a = int(input("Enter any year that is to be checked for leap year:",))
if a%4 == 0:
  if a%100 != 0:
    print("The given year is a leap year")
if a%400 == 0:
  print("The given year is a leap year")
else:
  print("It is not a leap year")