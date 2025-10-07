a = int(input("Enter any year that is to be checked for leap year: "))

if ( a % 4 == 0 and a % 100 != 0 ) or ( a % 400 == 0) :
	print("The given year is a leap year")
else :
	print("It is not a leap year")