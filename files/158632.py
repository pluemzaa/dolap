hrin = int(input())
minin = int(input())
hrout = int(input())
minout = int(input())
total = ((hrout*60)+minout)-((hrin*60)+minin)
if total %60 >0:
  x = (total // 60)+1
else:
  x = (total // 60)

if total <= 15:
  print('pay:0')
elif total < 180:
  print('pay:{}'.format(x*10))
elif total <= 360:
  print('pay:{}'.format((((x-3)*20)+30)))
else:
  print('pay:200')