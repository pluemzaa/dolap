x = int(input()) * 60
y = int(input())
z = int(input()) * 60
a = int(input())
b = (z - x) + (a - y)
if b <= 15:
  print('Pay:0')
elif (b > 15) and (b <= 180):
  c = ((b + 59) // 60) * 10
  print('Pay:{}'.format(c))
elif (b > 180) and (b <= 360):
  d = (((b + 59 - 180) // 60) * 20) + 30
  print('Pay:{}'.format(d))
else:
    print('Pay:200')