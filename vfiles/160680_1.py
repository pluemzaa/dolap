thin=int(input(""))
tmin=int(input(""))
thout=int(input(""))
tmout=int(input(""))
time_in = thin * 60 + tmin
time_out = thout * 60 + tmout
duration = time_out - time_in
if duration <= 15:
    fee = 0
elif duration <= 180:  
    hours = -(-duration // 60)  
    fee = hours * 10
elif duration <= 360:  
    total_hours = -(-duration // 60)
    if total_hours <= 3:
        fee = total_hours * 10
    else:
        fee = 3 * 10 + (total_hours - 3) * 20
else:
    fee = 200
print(f"Pay:{fee}")