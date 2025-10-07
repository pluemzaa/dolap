N=int(input("Enter a number (enter 0 to stop): "))
i=0
sum=0
while N!=0:
    sum+=N
    i+=1
    N=int(input("Enter a number (enter 0 to stop): "))
if i!=0:
    print("Average:",sum/i)
else:
    print("No numbers entered.")