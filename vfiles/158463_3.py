x = int(input("Enter any year that is to be checked for leap year:"))
if x%4 ==0 and x%100 !=0:
  print("The given year is a leap year")
elif x%400==0:
  print("The given year is a leap year") 
else:
      print("It is not a leap year")