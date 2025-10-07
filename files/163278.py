m = int(input())
k = int(input())
n = int(input())
answer = (m*k)
if answer % n == 0:
    answer = int((m*k)/n)
else:
    answer = int(((m*k)/n)+1)
print(answer)