time1 = int(input())
time2 = int(input())
time3 = int(input())
time4 = int(input())

t1 = time1 * 60
t3 = time3 * 60 

time_in = t1 + time2
time_out = t3 + time4

total = time_out - time_in
pay = 0
if (total > 360):
  print("Pay:",pay + 200)
elif (total >= 240) and (total <= 360 ):
  if total % 60 == 0:
    print("Pay:",pay + (total/60)*20)