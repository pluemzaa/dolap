# รับค่าจากผู้ใช้
vehicle_type = int(input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): "))
hours = float(input("Please enter the number of parking hours: "))

# ตรวจสอบค่าผิดพลาด
if vehicle_type not in [1, 2]:
    print("Invalid vehicle type")
elif hours <= 0:
    print("Please enter a valid number of parking hours")
elif hours < 1:
    print("Parking fee: 0.00 THB")
else:
    if vehicle_type == 1:
        # รถจักรยานยนต์
        first_hour = 10
        next_hour_rate = 5
    elif vehicle_type == 2:
        # รถยนต์ส่วนบุคคล
        first_hour = 30
        next_hour_rate = 15

    extra_hours = hours - 1
    fee = first_hour + (extra_hours * next_hour_rate)
    print(f"Parking fee: {fee:.2f} THB")