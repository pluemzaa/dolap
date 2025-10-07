in_hour = int(input(""))
in_min = int(input(""))
out_hour = int(input(""))
out_min = int(input(""))

convert_in_min = (in_hour*60) + in_min
convert_out_min = (out_hour*60) + out_min

calcurate = convert_out_min - convert_in_min
hour = int(calcurate//60)

if calcurate <= 15:
    pay = 0
    cal = 0
elif  calcurate < 240:
    pay = hour*10
    if calcurate%60 == 0:
        cal = 0
    else:
        cal = 10
    if calcurate > 180:
        if calcurate%60 == 0:
            cal = 0
        else:
            cal = 20
elif 240 <= calcurate <= 360:
    pay = hour*20
    if calcurate%60 == 0:
        cal = 0
    else:
        cal = 20
else:
    pay = 200
    cal = 0
pays = pay+cal
print(f"Pay:{pays}")