m = int(input(''))
k = int(input(''))
n = int(input(''))
ans = (m * k) / n
if ans % 1 == 0:
    print(int(ans))
else:
    ansnew = ((m * k) // n) + 1
    print(ansnew)