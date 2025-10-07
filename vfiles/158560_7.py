h_in = int(input())
m_in = int(input())
h_out = int(input())
m_out = int(input())

x = (h_in*60) + m_in
y = (h_out*60) + m_out
t = y-x

j=t//60
m=0
print("time",t)

if t<=15:
  print(t,j)
  print("Pay:0")
elif t<=180:
  if t%60==0:
    m=j*10
  else:
      m=j*10+10
  print(t,j)
  print(f'Pay:{m}')
elif t<=360:
  if t%60!=0:
    m+10
  else:
      m=j*10
  print(t,j)
  print(f'Pay:{j}')
else:
  print(t,j)
  print("Pay:200")