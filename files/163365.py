m = int(input(''))
k = int(input(''))
n = int(input(''))
r = (m*k)/n
r1 = r - int(r)
if 0 < r1 < 1:
    print(int(r) + 1)
else:
    print(int(r))