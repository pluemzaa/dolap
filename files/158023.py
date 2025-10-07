N= input("Enter a number (enter 0 to stop):")
N= float(N)
i=0
p=0
if N ==0:
    print("No numbers entered.")
else:
    while N != 0:
        p=p+N
        i=i+1
        N= input("Enter a number (enter 0 to stop):")
        N= float(N)
        Av=(p/i)
    print("Average:",Av)