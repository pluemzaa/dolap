number = input("enter a number:")
number = int(number)
if number > 0:
  print("{}is Positive".format(number))
elif number < 0:
  print("{}is Negative".format(number))
else:
  print("{}is zero".format(number))