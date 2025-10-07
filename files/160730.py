n = int(input("Enter any year that is to be checked for leap year:" ))

if  n%4 == 0 and n%100 != 0 :
    print("The given year is a leap year")
elif n%400 == 0:
    print(" The given year is a leap year")  
else:
    print("It is not a leap year")