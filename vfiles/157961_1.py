hin=int(input())
sin=int(input())
hout=int(input())
sout=int(input())
hsin=hin*60+sin
hsout=hout*60+sout
time=hsout-hsin
print(time)
if time<=15:
  print("Pay:0")
elif time<=180:
  ttime = (time-1)//60+1
  print(ttime)
  t = ttime*10
  print("Pay:",t)
elif time<=360:
  tttime = (time-1)//60+1-3
  print(tttime)
  t = tttime*20
  print("Pay:",t)
else:
  print("Pay:200")