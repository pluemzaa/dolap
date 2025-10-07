x = int(input("Enter a number (enter 0 to stop):"))
sum = 0
while x > 0:
  if x != 0:
      x = int(input("Enter a number (enter 0 to stop):"))
      sum += 1
  print(sum/x)