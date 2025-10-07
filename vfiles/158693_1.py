h1=int(input())
m1=int(input())
h2=int(input())
m2=int(input())
allin=h1*60+m1
allout=h2*60+m2
howlong=(allout-allin)
if howlong <=15:
  print("pay:0")
else :
  hours = (howlong+59)//60
  if hours <=3:
    print("pay:",hours*10)
  elif hours <=6 :
    print("pay:",30+(hours-3)*20)
  else:
    print("pay:200")