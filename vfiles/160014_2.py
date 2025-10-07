n=int(input("Enter a number (enter 0 to stop):"))
i=0
total=0
if n==0:
    print("No numbers entered.")
else:
    while n != 0 :
        total+=n
        i+=1
        n=int(input("Enter a number (enter 0 to stop):"))
    avg = total/i
    print(avg)