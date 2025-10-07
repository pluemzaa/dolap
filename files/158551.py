hrin=int(input())
minin=int(input())
hrout=int(input())
minout=int(input())

hrsum=hrout-hrin
minsum=minout-minin

if minsum < 0:
    minsum=minsum+60
if (hrsum==0) and (minsum<=15):
    print("Pay:0")
elif (hrsum==0) and (minsum>15) or (hrsum==1 and minsum==0):
    print("Pay:10")
elif (hrsum==1) and (minsum>0):
    print("Pay:20")
elif (hrsum==2) and (minsum>0) or (hrsum==3 and minsum==0):
    print("Pay:30")
elif (hrsum==3) and (minsum>0):
    print("Pay:50")
elif (hrsum==4) and (minsum>0):
    print("Pay:70")
elif (hrsum==5) and (minsum>0) or (hrsum==6 and minsum==0):
    print("Pay:90")
else :
    print("Pay:200")