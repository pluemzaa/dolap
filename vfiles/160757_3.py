x = float(input("Enter a number (enter 0 to stop):"))
sum = 0
total = 0
if x == 0:
  print("No numbers entered.")
while x != 0:
  sum += x
  total += 1
  x = float(input("Enter a number (enter 0 to stop):"))
  if x == 0:
    print ("Average:",sum/total)