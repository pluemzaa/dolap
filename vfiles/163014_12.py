x1 = int(input())
x2 = int(input())
x3 = int(input())
sum = (x1*x2)/x3
if sum %2 == 0:
    print(int(sum))
elif sum %2 != 0:
    print(int(sum+1))