year=input("Enter any year that is to be checked for leap year")
year=int(year)
if(year % 4 ==0 and year % 100 != 0) or (year % 400== 0):
  print("{} The given year is a leap year".format(year))
else :
  print("{} It is not a leap year".format(year))