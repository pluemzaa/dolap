vehicle_type = input("กรุณาเลือกประเภทรถ (1=รถจักรยานยนต์, 2=รถยนต์ส่วนบุคคล): ")

if vehicle_type not in ['1', '2']:
    print("Invalid vehicle type")
    exit()  
try:
    hours = float(input("กรุณากรอกจำนวนชั่วโมงที่จอด: "))
except ValueError:
    print("กรุณากรอกเป็นตัวเลขเท่านั้น")
    exit()

if hours <= 0:
    print("เวลาที่จอดต้องมากกว่า 0")
    exit()

if hours < 1:
    print("จอดฟรี")
    exit()

if vehicle_type == '1':  # รถจักรยานยนต์
    if hours <= 1:
        fee = 10
    else:
        fee = 10 + (int(hours) - 1) * 5
elif vehicle_type == '2':  # รถยนต์ส่วนบุคคล
    if hours <= 1:
        fee = 30
    else:
        fee = 30 + (int(hours) - 1) * 15

print(f"ค่าจอดรถคือ {fee} บาท")