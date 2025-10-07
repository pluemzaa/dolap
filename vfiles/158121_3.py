num = input("Enter any year that is to be checked for leap year:")
num = int(num)
if num %4==0 and num %400==0: 
  print("The given year is a leap year") 
elif num %100==0:
  print("It is not a leap year")     
else:
  print("It is not a leap year")