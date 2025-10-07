hour_1 = int(input())
min1 = int(input())
hour_2 = int(input())
min2 = int(input())
hour1 =hour_1*60
hour2 =hour_2*60
a = hour1+min1
b = hour2+min2
i =b-a
d =a+60
if i <=15:
  print("Pay:0")
elif i <= 119:
  print("Pay:10")
elif i <= 179:
   print("Pay:20")
elif i <= 239:
  print("Pay:30")
elif i <= 299:
  print("Pay:50")  
elif i<= 359:
  print("Pay:70") 
else:
  print("Pay:200")