h = int(input())
m = int(input())
ho = int(input())
mo = int(input())
k = h*60
l = ho*60
z = ((l+mo)-(k+m))
if z <=15:
  print("Pay:0")
elif 15 < z <=180:
  print("Pay:"+str((-((-z)//60))*10))
elif 180 < z <=360:
  print("Pay:"+str((30+(-((((-z)//60)+3)*20)))))
else:
  print("Pay:200")