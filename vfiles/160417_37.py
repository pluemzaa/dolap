records = []

while True:
    # รับชนิดรถ
    print("Please enter vehicle type (1: Motorcycle, 2: Personal Car): ", end="")
    try:
        vt = int(input())
    except:
        print("Invalid vehicle type")
        break

    if vt not in [1, 2]:
        print("Invalid vehicle type")
        break

    # รับจำนวนชั่วโมงจอด
    print("Please enter the number of parking hours: ", end="")
    try:
        hrs = float(input())
    except:
        print("Please enter a valid number of parking hours")
        break

    if hrs <= 0:
        print("Please enter a valid number of parking hours")
        break

    # คำนวณค่าจอด
    if hrs < 1:
        fee = 0.00
    elif vt == 1:
        fee = 10 + (hrs - 1) * 5
    else:
        fee = 30 + (hrs - 1) * 15

    print(f"Parking fee: {fee:.2f} THB")

    # เก็บข้อมูลเฉพาะเคสถูกต้อง
    records.append((vt, hrs, fee))

    # ถามว่าจะทำต่อไหม
    print("Do you want to continue? (y/n): ", end="")
    cont = input().strip().lower()
    print("-" * 30)
    if cont != "y":
        break

# แสดงสรุป
print("VT Hours Cost")
total = 0.0
for vt, hrs, fee in records:
    print(f"{vt} {hrs:.2f} {fee:.2f}")
    total += fee
print(f"Total {total:.2f} THB")