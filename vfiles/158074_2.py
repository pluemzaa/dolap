i=0
N=int(input("Enter a number (enter 0 to stop):"))
sum=0
while N!=0:
  i=i+1
  sum=sum+N
  x=sum/i
  N=int(input("Enter a number (enter 0 to stop):"))
print("Average:"x)