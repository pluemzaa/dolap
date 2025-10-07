n = int(input())
x = int(input())
y = int(input())
l = x*n
if l % y == 0:
    a = l/y
else:
    a = (l//y)+1
print(a)