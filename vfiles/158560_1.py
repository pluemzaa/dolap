import math
h_in = int(input())
m_in = int(input())
h_out = int(input())
m_out = int(input())

x = h_in*60 + m_in
y = h_out*60 + m_out
j= (x-y)/60
j=math.ceil(j)

_1 = (x<=15)
_2 = (15<x<180)
_3 = (240<x<360)
_4 = (x>360)

if _1:
  print("Pay:0")
elif _2:
  j=j*10
  print(f'{j}')
elif _3:
  j=j*20
  print(f'{j}')
else:
  print("Pay:200")