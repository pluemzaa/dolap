records = []

while True:
    # รับประเภทรถ
    vehicle_type = int(input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): "))
    
    if vehicle_type not in [1, 2]:
        hours = float(input("Please enter the number of parking hours: "))
        print("Invalid vehicle type")
        break
    
    # รับจำนวนชั่วโมง
    hours = float(input("Please enter the number of parking hours: "))
    
    if hours <= 0:
        print("Please enter a valid number of parking hours")
        continue_choice = input("Do you want to continue? (y/n): ")
        if continue_choice == 'y':
            print("------------------------------")
            continue
        else:
            break
    
    # คำนวณค่าจอด
    if hours < 1:
        fee = 0.00
    elif vehicle_type == 1:  # Motorcycle
        fee = 10 + (hours - 1) * 5 if hours > 1 else 10
    else:  # Personal Car
        fee = 30 + (hours - 1) * 15 if hours > 1 else 30
    
    print(f"Parking fee: {fee:.2f} THB")
    records.append((vehicle_type, hours, fee))
    
    # ถามต่อ
    continue_choice = input("Do you want to continue? (y/n): ")
    if continue_choice != 'y':
        break
    print("------------------------------")

# แสดงสรุป
if records:
    print("------------------------------")
    print("VT Hours Cost")
    total = 0
    for vehicle_type, hours, fee in records:
        print(f"{vehicle_type} {hours:.2f} {fee:.2f}")
        total += fee
    print(f"Total {total:.2f} THB")