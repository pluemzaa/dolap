N=float(input("Enter a number (enter 0 to stop):")) 
sum=0
count=0
if  N == 0:
  print("No numbers entered.")
while N !=0:
  sum += N
  count += 1
  N=float(input("Enter a number (enter 0 to stop):")) 
  if N == 0:
    print("Averege:",sum/count)