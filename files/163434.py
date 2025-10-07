e = int(input(""))
w = int(input(""))
r = int(input(""))
t = (e*w)/r
u = (e*w)%r
if u == 0 : 
    print(int(t))
else:
    t+=1 
    print(int(t))