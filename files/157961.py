hin=int(input())
sin=int(input())
hout=int(input())
sout=int(input())

tall = (hout*60+sout)-(hin*60+sin)
if tall<=15:
    print("Pay:0")
elif tall<=180:
    ttall = (tall+59)//60
    t = ttall*10
    print("Pay:",t)
elif tall<=360:
    Tall=(tall-180)
    tt=((Tall+59)//60)*20
    ttt=(180//60)*10
    T=tt+ttt
    print("Pay:",T)
else:
    print("Pay:200")