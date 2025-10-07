hours_in = int(input(""))
minutes_in = int(input(""))
hours_out = int(input(""))
minutes_out = int(input(""))
hrs_result = hours_out - hours_in
minutes_result = minutes_out - minutes_in
Pay = 0
x = 0
'''
1. จอดรถไม่เกิน 15 นาที ไม่คิดค่าบริการ
2. จอดรถเกิน 15 นาที แต่ไม่เกิน 3 ชั่วโมง คิดค่าบริการชั่วโมงละ 10 บาท เศษของชั่วโมงคิดเป็นหนึ่งชั่วโมง
3. จอดรถตั้งแต่ 4 ชั่วโมง ถึง 6 ชั่วโมง คิดค่าบริการชั่วโมงที่ 4-6 ชั่วโมงละ 20 บาท เศษของชั่วโมงคิดเป็นหนึ่งชั่วโมง
4. จอดรถเกิน 6 ชั่วโมงขึ้นไป เหมาจ่ายวันละ 200 บาท
'''
if minutes_result <= 15 and hrs_result == 0:
    print("Pay:{}".format(Pay))
elif hrs_result == 1 and minutes_result == 0:
    Pay = hrs_result*10
    print("Pay:{}".format(Pay))
elif hrs_result == 2 and minutes_result == 0:
    Pay = hrs_result*10
    print("Pay:{}".format(Pay))
elif minutes_result >= 0 and hrs_result < 3:
    hrs_result += 1
    Pay = hrs_result*10
    print("Pay:{}".format(Pay))
elif minutes_result == 0 and hrs_result == 3:
    Pay = hrs_result*10
    print("Pay:{}".format(Pay))


elif 0 <= hrs_result <= 3 or hrs_result > 3 and hrs_result <= 5:
    if hrs_result == 3 and minutes_result > 0:
        Pay = 3*10
        x += 1
        x *= 20
    elif hrs_result == 4 and minutes_result == 0:
        Pay = 3*10
        x += 1
        x *= 20
    elif hrs_result == 4 and minutes_result > 0:
        Pay = 3*10
        x += 2
        x *= 20
    elif hrs_result == 5 and minutes_result == 0:
        Pay = 3*10
        x += 2
        x *= 20
    elif hrs_result == 5 and minutes_result > 0:
        Pay = 3*10
        x += 3
        x *= 20
    Pay += x
    
    
    

    print("Pay:{}".format(Pay))

elif hrs_result == 6 and minutes_result == 0:
    Pay = 3*10
    x += 3
    x *= 20
    Pay += x
    print("Pay:{}".format(Pay))
elif hrs_result == 6 and minutes_result > 0:
    Pay += 200
    print("Pay:{}".format(Pay))