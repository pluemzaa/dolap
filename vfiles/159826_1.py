Avg = 0
i = 0
number = int(input("Enter a number (enter 0 to stop):"))
while number != 0:
  i = i + 1
  Avg = (Avg + number)/i
number = int(input("Enter a number (enter 0 to stop):"))

print("Average: ",Avg)