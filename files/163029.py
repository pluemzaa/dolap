m = int(input(""))
k = int(input(""))
n = int(input(""))
mm = k*m
if mm%n==0:
    nn = mm/n
    print(nn)
else:
    nn = (mm//n) + 1
    print(nn)