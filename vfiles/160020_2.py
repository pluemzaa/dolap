i=1
sum=0
N=0
number=float(input('Enter a number (enter 0 to stop):'))
while number!=0:
    sum=sum+number
    N=N+1
    number=float(input('Enter a number (enter 0 to stop):'))
if sum==0:
    print('No numbers entered.')
else:
    print('Average:',sum/N)