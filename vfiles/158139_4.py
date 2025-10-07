h=int(input())
m=int(input())
t=int(input())
p=int(input())
f((t*60)+p)-((h*60)+m)
if f<=15:
  print('Pay:0')
elif f<=180:
  print('Pay:',((f+59)//60)*10)
  f<=360
elif f<=360:
  F=(f-180)
  J=((F+59)//60)*20
  i=(180//60)*10
  sum=J+i
  print ('Pay:',sum)
else
  print('Pay:200')