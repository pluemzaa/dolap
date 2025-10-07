"""
จงเขียนโปรแกรมสำหรับคำนวณค่าจอดรถสำหรับร้านรับฝากรถแห่งหนึ่ง

โดยโปรแกรมจะรับชนิดของรถ 1. รถจักรยานยนต์ 2. รถยนต์ส่วนบุคคล และรับเวลาที่จอด (หน่วยเป็นชั่วโมง) โดยจะคำนวณเงินจากเงื่อนไขต่างๆ ดังนี้

1. รถจักรยานยนต์ จะคิดค่าจอด 1 ชั่วโมงแรกชั่วโมงละ 10 บาท ชั่วโมงโมงต่อไป 5 บาท

2. รถยนต์ส่วนบุคคล จะคิดค่าจอด 1 ชั่วโมงแรกชั่วโมงละ 30 บาท ชั่วโมงโมงต่อไป 15 บาท

3. จอดไม่ถึง 1 ชั่วโมงจอดฟรีทั้ง รถจักรยานยนต์รถยนต์ส่วนบุคคล

5. หากผู้ใช้เลือกประเภทรถนอกเหนือจาก จะต้องแสดงข้อความแจ่งเตือน แล้วจบโปรแกรม
"""

vehType = int(input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): "))
h = float(input("Please enter the number of parking hours: "))
 
if vehType >= 1 and vehType <= 2:
    if h > 0:
        if h >= 1:
            if vehType == 1:
                print(f"Parking fee: {((h-1)*5)+10:.2f} THB")
            else:
                print(f"Parking fee: {((h-1)*15)+30:.2f} THB")
        else:
            print(f"Parking fee: 0.00 THB")
    else:
        print("Please enter a valid number of parking hours")
else:
    print("Invalid vehicle type")
# Please enter vehicle type (1: Motorcycle, 2: Personal Car): 1
# Please enter the number of parking hours: 3.5
# Parking fee: 22.50 THB

# Please enter vehicle type (1: Motorcycle, 2: Personal Car): 3
# Please enter the number of parking hours: 4
# Invalid vehicle type

# Please enter vehicle type (1: Motorcycle, 2: Personal Car): 1
# Please enter the number of parking hours: -3
# Please enter a valid number of parking hours