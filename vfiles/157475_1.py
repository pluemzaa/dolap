hour1=int(input())>=7
min1=int(input())<=60
hour2=int(input())<=23
min2=int(input())<=60
park=hour1+(min1/60)
out=hour2+(min2/60)
if (park-out)<=0.25:
    print("pay:0")
elif 0.25<=(park-out)<=3:
    print("pay:10")
elif (hour2<=6)>(hour1>=4):
    print("pay:20")
else:
    print("pay:200")