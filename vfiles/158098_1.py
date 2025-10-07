N=int(input('Enter a number (enter 0 to stop):' ))
a=0
b=0
while N>0 :
    if N !=0 :
       a=a+N
       N=int(input('Enter a number (enter 0 to stop):' ))
       b=b+1
b=b-1
print(a/b)