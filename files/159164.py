# รับข้อมูลจากผู้ใช้
vehicle_type = input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): ")
try:
    hours = float(input("Please enter the number of parking hours: "))

    # ตรวจสอบจำนวนชั่วโมงก่อน
    if hours <= 0:
        print("Please enter a valid number of parking hours")
    # ตรวจสอบประเภทรถ
    elif vehicle_type not in ['1', '2']:
        print("Invalid vehicle type")
    else:
        # คำนวณค่าจอดรถ
        if hours < 1:
            fee = 0.0
        else:
            if vehicle_type == '1':  # Motorcycle
                fee = 10 + (hours - 1) * 5
            else:  # vehicle_type == '2' Personal Car
                fee = 30 + (hours - 1) * 15

        print(f"Parking fee: {fee:.2f} THB")

except ValueError:
    print("Please enter a valid number of parking hours")