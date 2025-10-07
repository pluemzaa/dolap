import math
h_in = int(input())
m_in = int(input())
h_out = int(input())
m_out = int(input())

x = h_in*60 + m_in
y = h_out*60 + m_out
th = x-y//60
tm = x-y%60
j= (x-y)/60
j=math.ceil(j)

#_1 = (x<=15)
#_2 = (15<x<180)
#_3 = (240<x<360)
#_4 = (x>360)

if tm <= 15 :
  print("Pay:0")
elif 15<th<180:
  j=j*10
  print(f'Pay:{j}')
elif 240<th<360:
  j=j*20
  print(f'Pay:{j}')
else:
  print("Pay:200")