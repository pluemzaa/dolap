IN_h = int(input())
IN_m = int(input())
OUT_h = int(input())
OUT_m = int(input())

IN = (IN_h*60)+IN_m
OUT = (OUT_h*60)+OUT_m
time = OUT-IN

if time <= 15:
    print("Pay:0")
elif time <= 180:
    print ("Pay:",(-(-time//60)*10)),sep=""
elif time <= 360:
    print ("Pay:",(30+(-((-time//60)+3))*20))
else :
    print ("Pay:200")