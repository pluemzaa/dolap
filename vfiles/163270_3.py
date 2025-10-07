m = int(input(''))
k = int(input(''))
n = int(input(''))
r = (m*k)
rr = r/n 
if r % n != 0:
    rr+=1

print (int(rr))