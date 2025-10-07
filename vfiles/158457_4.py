year = int(input('Enter any year that is to be checked for leap year'))
if (year%4==0 and year%100 !=0)or(year%400==0):
      print("the given year ia a leap year")
else:
      print("it is not a leap year")