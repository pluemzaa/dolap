n=int(input("enter"))
a,b=0,1
for i in range(n):
    print(a,end=" ")
    x=a+b
    a=b
    b=x