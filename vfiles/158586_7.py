num = int(input("Enter any year that is to be checked for leap year:"))
num = num-543
if num % 4 == 0 |num % 400 == 0:
  print("The given year is a leap year") 
elif num % 100 !=0:
  print("It is not a leap year")   
else :
  print("The given year is a leap year")