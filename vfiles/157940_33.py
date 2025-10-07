num = int(input('Enter any year that is to be checked for leap year:'))
if (num % 400 == 0) and (num % 4 == 0) or (num %100 != 0):
 print('The given year is a leap year')
else:
 print('It is not a leap year')