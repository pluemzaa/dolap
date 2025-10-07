inh = int(input())
inm = int(input())
outh = int(input())
outm = int(input())
in_time = inh * 60 + inm
out_time = outh * 60 + outm
time = out_time - in_time
if time % 60 == 0:
    hours = time // 60
else:
    hours = time // 60 + 1
if time <= 15:
    pay = 0
elif time <= 180:  
    pay = hours * 10
elif time <= 360:  
    first_3_hours = 3 * 10
    remaining_hours = hours - 3
    pay = first_3_hours + (remaining_hours * 20)
else:  
    pay = 200
print("Pay:" + str(pay))