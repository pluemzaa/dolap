N = int(input("Enter a number (enter 0 to stop):"))
i=0
total=0
if N == 0:
    print("No numbers entered.")
else:
    while N != 0:
        total+=N
        i+=1
        N = int(input("Enter a number (enter 0 to stop):"))
    avg = total/i
    print(avg)