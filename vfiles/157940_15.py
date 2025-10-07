num = int(input('Enter any year that is to be checked for leap year:')
if num % 400 == 0:
    print('The given year is a leap year')
if num % 4 == 0:
    print('The given year is a leap year')
if num % 100 != 0:
    print('It is not a leap year')