hour_1 = int(input())
min_1 = int(input())
hour_2 = int(input())
min_2 = int(input())
hour_1 = hour_1*60
hour_2 = hour_2*60
a = hour1+min1
b = hour2+min2
c = b-a
d = a+60
if c <= 15:
    print("Pay:0")
elif  c <= 119 : 
  print("Pay:10")
elif  c <=179: 
  print("Pay:20")
elif c <=239:  
  print("Pay:30")
elif  c <=299  : 
  print("Pay:50")
elif  c <=359: 
  print("Pay:70")
else: 
  print("Pay:200")