records = []  # เก็บรายการที่ถูกต้องเท่านั้น

while True:
    # รับชนิดรถ และชั่วโมง (ให้เว้นวรรคหลังโคลอนตามโจทย์)
    print("Please enter vehicle type (1: Motorcycle, 2: Personal Car): ", end="")
    vt_raw = input()
    print("Please enter the number of parking hours: ", end="")
    hrs_raw = input()

    # แปลงค่าและตรวจสอบความถูกต้อง
    ok_type = True
    ok_hours = True
    try:
        vt = int(vt_raw)
    except:
        ok_type = False

    try:
        hrs = float(hrs_raw)
    except:
        ok_hours = False
        hrs = 0.0

    # เคสผิด: ประเภทไม่ใช่ 1 หรือ 2
    if (not ok_type) or (vt not in [1, 2]):
        print("Invalid vehicle type")

    # เคสผิด: ชั่วโมงแปลงไม่ได้ หรือ <= 0
    elif (not ok_hours) or (hrs <= 0):
        print("Please enter a valid number of parking hours")

    else:
        # คำนวณค่าจอด
        if hrs < 1:
            fee = 0.00
        elif vt == 1:              # Motorcycle
            fee = 10 + (hrs - 1) * 5
        else:                      # Personal Car
            fee = 30 + (hrs - 1) * 15

        # แสดงผลค่าจอด (ฟรีต้องเป็น 00.00)
        fee_str = "00.00" if fee == 0 else f"{fee:.2f}"
        print(f"Parking fee: {fee_str} THB")

        # เก็บเฉพาะรายการถูกต้อง
        records.append((vt, hrs, fee))

    # ถามว่าจะทำต่อไหม
    print("Do you want to continue? (y/n): ", end="")
    cont = input().strip().lower()
    print("------------------------------")
    if cont != "y":
        break

# สรุปผล
print("VT Hours Cost")
total = 0.0
for vt, hrs, fee in records:
    print(f"{vt} {hrs:.2f} {fee:.2f}")
    total += fee
print(f"Total {total:.2f} THB")