number = input("Enter a number:")
number = int(number)
if number > 0:
  print("{}Is Positive".format(number))
elif number < 0:
  print("{}Is Negative".format(number))
else:
  print("{}Is Zero".format(number))