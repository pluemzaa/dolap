n=int(input("Enter any year that is 2000:"))
if (year % 4==0 and (year % 100 !=0) or (year % 400 ==0)
    print(n,"The given year is a leap year")
else:
  print(n,"It is not a leap year")