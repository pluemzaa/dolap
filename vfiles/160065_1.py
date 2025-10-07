x=int(input("Enter input:"))
for a in range(1, x + 1):
    N=0
    for b in range(1, a+1 ):
        if a%b==0:
            N=N+1
    if N==2:
        print(a)