x = int(input("Enter a number (enter 0 to stop):"))
sum = 0
count = 0
while x != 0:
  sum += x
  count += 1
  x = int(input("Enter a number (enter 0 to stop):"))
  if x == 0:
    print ("Average: "sum/count)