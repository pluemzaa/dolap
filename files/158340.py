in_h = int(input())
in_m = int(input())
out_h = int(input())
out_m = int(input())
in_tt = in_h * 60 + in_m
out_tt = out_h * 60 + out_m
duration = out_tt - in_tt
if duration <= 15:
    fee = 0
elif duration <= 180:
    h = (duration + 59) // 60
    fee = h * 10
elif duration <= 360:
    h = (duration + 59) // 60
    f3 = 3 * 10
    re = (h - 3) * 20
    fee = f3 + re
else:
    fee = 200
print(f"Pay: {fee}")