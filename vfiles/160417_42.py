records = []          # เก็บเฉพาะรายการถูกต้อง

while True:
    print("Please enter vehicle type (1: Motorcycle, 2: Personal Car): ", end="")
    vt_raw = input()
    print("Please enter the number of parking hours: ", end="")
    hrs_raw = input()

    # ตรวจชนิดรถและชั่วโมง
    ok_type, ok_hours = True, True
    try:
        vt = int(vt_raw)
    except:
        ok_type = False
    try:
        hrs = float(hrs_raw)
    except:
        ok_hours, hrs = False, 0.0

    if (not ok_type) or vt not in [1, 2]:
        print("Invalid vehicle type")
    elif (not ok_hours) or hrs <= 0:
        print("Please enter a valid number of parking hours")
    else:
        # คำนวณค่าจอด
        if hrs < 1:
            fee = 0.00
        elif vt == 1:                # Motorcycle
            fee = 10 + (hrs - 1) * 5
        else:                        # Personal Car
            fee = 30 + (hrs - 1) * 15
        print(f"Parking fee: {fee:.2f} THB")   # ← ใช้ .2f ปกติ

        records.append((vt, hrs, fee))         # เก็บรายการที่ถูกต้อง

    # ถามต่อ
    print("Do you want to continue? (y/n): ", end="")
    cont = input().strip().lower()
    if cont != "y":
        break
    print("------------------------------")

# สรุปรายการ
print("VT Hours Cost")
total = 0.0
for vt, hrs, fee in records:
    print(f"{vt} {hrs:.2f} {fee:.2f}")
    total += fee
print(f"Total {total:.2f} THB")