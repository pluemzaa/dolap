h = float(input())
m = float(input())
k = float(input())
q = float(input())
l = m/60
n = q/60
r = (k - h) + (n - l)
if r <= 15/60:
    print('Pay:0')
elif (r >= 15/60) and (r <= 3.00):
    p = (r // r) + 1
    print('Pay:',p * 10)
elif (r >= 4.00) and (r <= 6.00):
    v = (r // r) + 1
    print('Pay:',v * 20)
else:
    print('Pay:200')