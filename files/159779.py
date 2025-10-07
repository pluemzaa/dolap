p=int(input())
a=int(input())
t=int(input())
y=int(input()) 
f=((t*60)+y)-((p*60)+a)
if f<=15:
  print('pay:0')
elif f<=180:
  print('pay:',((f+59)//60)*10)
  f<=360
elif f<=360:
  F=(f-180)
  J=((F+59)//60)*20
  i=(180//60)*10
  sum=J+i
  print ('pay:',sum)
else:
  print('pay:200')