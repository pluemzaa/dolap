hello =int(input('Enter any year that is to be checked for leap year: '))
if (hello %400 ==0) or  ((hello % 4 == 0) and (hello% 100 !=0)):
  print('The given year is a leap year')
else:
  print('It is not a leap year')