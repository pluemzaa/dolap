m = int(input(""))
k = int(input(""))
n = int(input(""))
a = (m*k)//n
if (m*k) % n != 0:
    a+=1
print(a)