sum=0
i=0
n = float(input("Enter a number (enter 0 to stop): "))
while n!=0:
  sum=sum+n
  i=i+1
  n = float(input("Enter a number (enter 0 to stop): "))
if i!=0:
  print("Average:",sum/i)
else :
  print("No numbers entered.")