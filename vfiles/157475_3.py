hour1=int(input())
min1=int(input())
hour2=int(input())
min2=int(input())
park=hour1+(min1/60)
out=hour2+(min2/60)
if (out-park)<=0.25:
    print("pay:0")
elif 0.25<=(out-park)and(out-park)<=3 or(out-park)>3 and (out-park)<4 :
    print("pay:10")
elif (4<=park) and (out<=6):
    print("pay:20")
else:
    print("pay:200")