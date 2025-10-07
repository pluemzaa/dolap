Y = int(input('Enter any year that is to be checked for leap year:'))
if (Y%4==0) and (Y%100!=0) or (Y%400==0):
   print('The given year is a leap year')
else :
    print('It is not a leap year')