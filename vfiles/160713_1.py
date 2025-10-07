# โปรแกรมคำนวณค่าจอดรถ
records = []  # เก็บข้อมูลที่ถูกต้อง

while True:
    print("Please enter vehicle type (1: Motorcycle, 2: Personal Car): ", end="")
    vehicle = input()
    print("Please enter the number of parking hours: ", end="")
    try:
        hours = float(input())
    except:
        print("Please enter a valid number of parking hours")
        print("Do you want to continue? (y/n): ", end="")
        if input().lower() != 'y':
            break
        print("------------------------------")
        continue

    if vehicle not in ["1", "2"]:
        print("Invalid vehicle type")
    elif hours <= 0:
        print("Please enter a valid number of parking hours")
    else:
        if hours < 1:
            fee = 0.00
        elif vehicle == "1":  # Motorcycle
            fee = 10 + (hours - 1) * 5
        elif vehicle == "2":  # Personal Car
            fee = 30 + (hours - 1) * 15
        print(f"Parking fee: {fee:.2f} THB")
        records.append((vehicle, hours, fee))

    print("Do you want to continue? (y/n): ", end="")
    if input().lower() != 'y':
        break
    print("------------------------------")

# สรุปรายการ
print("------------------------------")
print("VT Hours Cost")
total = 0
for v, h, f in records:
    print(f"{v} {h:.2f} {f:.2f}")
    total += f
print(f"Total {total:.2f} THB")