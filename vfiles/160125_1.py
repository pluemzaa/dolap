# รับประเภทของรถ
vehicle_type = input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): ")

# ตรวจสอบประเภทของรถ
if vehicle_type not in ["1", "2"]:
    print("Invalid vehicle type")
else:
    # แปลงเป็นจำนวนเต็ม
    vehicle_type = int(vehicle_type)

    # รับจำนวนชั่วโมง
    try:
        parking_hours = float(input("Please enter the number of parking hours: "))
    except ValueError:
        print("Please enter a valid number of parking hours")
        exit()

    # ตรวจสอบว่าจำนวนชั่วโมงต้อง > 0
    if parking_hours <= 0:
        print("Please enter a valid number of parking hours")
    # จอดไม่ถึง 1 ชั่วโมง
    elif parking_hours < 1:
        print("Parking fee: 0.00 THB")
    else:
        # รถจักรยานยนต์
        if vehicle_type == 1:
            first_hour_rate = 10
            next_hour_rate = 5
        # รถยนต์ส่วนบุคคล
        else:
            first_hour_rate = 30
            next_hour_rate = 15

        # คำนวณค่าจอด
        total_fee = first_hour_rate + (parking_hours - 1) * next_hour_rate
        print(f"Parking fee: {total_fee:.2f} THB")