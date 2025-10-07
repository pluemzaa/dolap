year=input("Enter any year that is to be checked for leap year:")
year=int(year)
if year%4==0:
  if year%100!=0:
    print("The given year is leap year")
  else:
    if year%400==0:
      print("The given year is leap year")
    else:
      print("It is not a leap year")