i=0
N=int(input("Enter a number (enter 0 to stop):"))
sum=0
while N!=0:
    i=i+1
    sum=sum+N
    N=int(input("Enter a number (enter 0 to stop):"))
if i!=0:
    x=sum/i
    print("Average:",x)
else:
    print("No numbers entered.")