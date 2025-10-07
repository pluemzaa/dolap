num_str = input("Enter any year that is to be checked for leap year: ")
num = int(num_str)
if (num % 4 == 0 and num % 100 != 0) or (num % 400 == 0):
    print("The given year is a leap year")
else:
    print("It is not a leap year")