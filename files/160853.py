records = []

while True:
    try:
        vehicle_type = int(input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): "))
        hours = float(input("Please enter the number of parking hours: "))
    
        if vehicle_type not in [1, 2]:
            print("Invalid vehicle type")
       
        elif hours <= 0:
            print("Please enter a valid number of parking hours")
        else:
            # จอดไม่ถึง 1 ชั่วโมง ฟรี
            if hours < 1:
                fee = 0.00
            else:
                if vehicle_type == 1:
                    # รถจักรยานยนต์
                    fee = 10 + (hours - 1) * 5
                elif vehicle_type == 2:
                    # รถยนต์ส่วนบุคคล
                    fee = 30 + (hours - 1) * 15

            print(f"Parking fee: {fee:.2f} THB")
            records.append((vehicle_type, hours, fee))
    except ValueError:
        print("Invalid input format")
        break
    

    
    # ถามว่าจะทำต่อหรือไม่
    cont = input("Do you want to continue? (y/n): ").strip().lower()
    print("-" * 30)
    if cont != 'y':
        break

# สรุปรายการ
print("VT Hours Cost")
total = 0
for rec in records:
    vt, h, c = rec
    print(f"{vt} {h:.2f} {c:.2f}")
    total += c

print(f"Total {total:.2f} THB")