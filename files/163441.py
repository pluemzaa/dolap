m=int(input(""))
k=int(input(""))
n=int(input(""))
totalitem=m*k
bags=totalitem//n
if bags % n <=0:
    bags += 2
print(int(bags))