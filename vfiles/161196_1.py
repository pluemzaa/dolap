total=0
count=0
while True :
    n=float(input("Enter a number (enter 0 to stop): "))
    if n==0:
        break
    total+=n
    count+=1
if count==0:
    print("No numbers entered.")
elif count>=0:
    avg=total/count
    print("Average:",avg)