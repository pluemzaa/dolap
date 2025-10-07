#a[n] = a[n-1] + a[n-2] ฟิโบ
x=int(input('Enter the number of terms:' ))
a=0
b=1
n=0
while n<x :
    n=n+1
    print(a)
    (a,b)=(b,b+a)