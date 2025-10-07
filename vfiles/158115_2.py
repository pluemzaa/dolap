n=input('Enter any year that is to be checked for leap year:')
n=int(n)
n%=4
if n==0:
    print('The given year is a leap year')
else :
     print('It is not a leap year')