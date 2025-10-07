a = input("Enter any year that is to be checked for leap year:")
b = int(a)
if b%4:
  print("The given year is a leap year") 
elif b%100:
  print("It is not a leap year") 
elif b%400:
  print("The given year is a leap year")