years = int(input('Enter any year that is to be checked for leap year:'))
if years % 4 ==0 and years % 400 == 0:
    print('The given year is a leap year')
elif years % 100 != 0:
    print('It is not a leap year')
else:
    print('It is not a leap year')