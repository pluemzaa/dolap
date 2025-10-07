h_in=int(input())
m_in=int(input())
h_out=int(input())
m_out=int(input())
time_in=h_in*60+m_in
time_out=h_out*60+m_out

time=time_out-time_in

if time<=15:
  print("Pay:0")
elif 15<=time<=180:
  print("Pay:"+str(-(-time//60)*10))
elif 180<time<=360:
  print("Pay:"+str(30+(-((-time//60)+3)*20)))
else:
  print("Pay:200")