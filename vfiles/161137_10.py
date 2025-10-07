def calculate_parking_fee(vehicle_type, hours):
    # ชั่วโมง < 1 ฟรี
    if hours < 1:
        return 0.00
    if vehicle_type == "1":            # รถจักรยานยนต์
        return 10 + (hours-1)*5
    elif vehicle_type == "2":          # รถยนต์ส่วนบุคคล
        return 30 + (hours-1)*15

records = []

while True:
    print("Please enter vehicle type (1: Motorcycle, 2: Personal Car): ", end='')
    vehicle_type = input().strip()
    # ตรวจสอบชนิดรถ
    if vehicle_type not in ("1", "2"):
        print("Invalid vehicle type")
        break

    print("Please enter the number of parking hours: ", end='')
    try:
        hours_input = input().strip()
        hours = float(hours_input)
    except ValueError:
        print("Please enter a valid number of parking hours")
        break

    # ตรวจสอบจำนวนชั่วโมง
    if hours <= 0:
        print("Please enter a valid number of parking hours")
        break

    # คำนวณค่าใช้จ่าย
    fee = calculate_parking_fee(vehicle_type, hours)
    print(f"Parking fee: {fee:.2f} THB")
    records.append((vehicle_type, hours, fee))

    print("Do you want to continue? (y/n): ", end='')
    cont = input().strip().lower()
    print("------------------------------ ( copy ไปเลย)")
    if cont != 'y':
        break

# สรุป ยอด
if len(records) > 0:
    print("VT Hours Cost")
    total = 0
    for vt, hr, fee in records:
        print(f"{vt} {hr:.2f} {fee:.2f}")
        total += fee
    print(f"Total {total:.2f} THB")