a = int(input())
b = int(input())
c = int(input())
a = a*b
w = a//c
if a%c != 0:
    w+=1
print(w)