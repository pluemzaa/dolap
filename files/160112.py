n=int(input("Enter a number (enter 0 to stop):"))
t=0
i=0
while n != 0:
  t=t+n
  i=i+1
  n=int(input("Enter a number (enter 0 to stop):"))
if i > 0:
  avg = t/i
  print("Average:", avg)
else :
  print("No numbers entered.")