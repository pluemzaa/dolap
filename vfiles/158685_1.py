x = int(input()) * 60
y = int(input()) * 60
z = int(input()) * 60
a = int(input())
b = x // 60 * 60
c = y // 60 * 60
r = (z - x) + (a - y)

if r <= 15:
    print("pay:0")
elif (r > 15) and (r <= 180):
    p = ((r + 59) // 60) * 10
    print("pay:", p)
elif (r <= 240) and (r <= 360):
    l = ((r + 59) // 60) * 20 - ((180 + 59) // 60) * 10
    print("pay:", l)
else:
    print("pay:", 200)