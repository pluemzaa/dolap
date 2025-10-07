p=int(input())
a=int(input())
y=int(input())
s=int(input())
f((y*60)+s)-((p*60)+a)
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
else:
  print('Pay:200')