sum = 0
number_arai = 0
input_ = int(input("Enter a number (enter 0 to stop):"))
while input_ != 0:
  number_arai = number_arai +1
  sum = sum + input_
  input_ = int(input("Enter a number (enter 0 to stop):"))
  average = sum/number_arai
if number_arai == 0:
  print("No numbers entered.")
else:
  print("Average:",average)