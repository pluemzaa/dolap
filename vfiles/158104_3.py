years = input('Enter any year that is to be checked for leap years:')

if years%4 == 0:
  print('The given year is a leap year')
elif years%400 and years%100 != 0:
  print('The given year is a leap year')
else:
  print('It is not a leap year')