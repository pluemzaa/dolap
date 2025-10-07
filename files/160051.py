N=int(input("Enter a number N: "))
for i in range(2,N+1):
    if all(i%j!=0 for j in range(2,i)):
        print(i)