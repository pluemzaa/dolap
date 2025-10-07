total=0
count=0
while True:
    n=int(input("Enter a number(enter 0 to stop):"))
    if n==0:
        break
        total+=n
        count+=1
        if count > 0:
            average=total/count
            print("Average:,average")
        else:
            print("No numbers entered")