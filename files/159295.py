# จงเขียนโปรแกรมสำหรับคำนวณค่าจอดรถสำหรับร้านรับฝากรถแห่งหนึ่ง
# โดยโปรแกรมจะรับชนิดของรถ 1. รถจักรยานยนต์ 2. รถยนต์ส่วนบุคคล และรับเวลาที่จอด (หน่วยเป็นชั่วโมง) โดยจะคำนวณเงินจากเงื่อนไขต่างๆ ดังนี้
# 1.รถจักรยานยนต์ จะคิดค่าจอด 1 ชั่วโมงแรกชั่วโมงละ 10 บาท ชั่วโมงโมงต่อไป 5 บาท
# 2.รถยนต์ส่วนบุคคล จะคิดค่าจอด 1 ชั่วโมงแรกชั่วโมงละ 30 บาท ชั่วโมงโมงต่อไป 15 บาท
# 3.จอดไม่ถึง 1 ชั่วโมงจอดฟรีทั้ง รถจักรยานยนต์รถยนต์ส่วนบุคคล
# 5.หากผู้ใช้เลือกประเภทรถนอกเหนือจาก จะต้องแสดงข้อความแจ่งเตือน แล้วจบโปรแกรม
# Invalid vehicle type
# 5. ผู้ใช้งานจะต้องป้อนจำนวนชั่วมากกว่า 0 ป้อนตัวเลขน้อยกว่าหรือเท่ากับ 0 จะต้องแสดงข้อความแจ่งเตือน แล้วจบโปรแกรม
# Please enter a valid number of parking hours
# ตัวอย่างผัลลัพธ์ #1
# Please enter vehicle type (1: Motorcycle, 2: Personal Car): 1
# Please enter the number of parking hours: 3.5
# Parking fee: 22.50 THB

w = int(input("Please enter vehicle type (1: Motorcycle, 2: Personal Car):"))
s = float(input("Please enter the number of parking hours:"))
a = 0

if w>2:
    print("Invalid vehicle type")
elif s<=0:
    print("Please enter a valid number of parking hours")
elif s>0 and s<1:
    print("Parking fee: 0.00 THB")
else:
    if w==1:
        a = ((s-1)*5)+10
        print(f"Parking fee:{a:.2f} THB")
    else:
        a = ((s-1)*15)+30
        print(f"Parking fee:{a:.2f} THB")