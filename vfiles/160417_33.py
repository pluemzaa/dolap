records = []  # เก็บเฉพาะรายการที่ถูกต้องเท่านั้น

while True:
    # รับชนิดรถ
    print("Please enter vehicle type (1: Motorcycle, 2: Personal Car): ", end="")
    vt_raw = input()

    # รับชั่วโมงจอด (รับทุกครั้ง เพื่อให้เอาต์พุตตรงลำดับกับตัวอย่าง)
    print("Please enter the number of parking hours: ", end="")
    hrs_raw = input()

    # ตีความค่า
    valid_type = True
    try:
        vt = int(vt_raw)
    except:
        valid_type = False

    valid_hours_num = True
    try:
        hrs = float(hrs_raw)
    except:
        valid_hours_num = False
        hrs = 0.0  # ค่าใดๆก็ได้ เพราะจะถือว่า invalid

    # ตัดสินใจ/แสดงผล
    if (not valid_type) or (vt not in [1, 2]):
        print("Invalid vehicle type")

    elif (not valid_hours_num) or (hrs <= 0):
        print("Please enter a valid number of parking hours")

    else:
        # คำนวณค่าจอด
        if hrs < 1:
            fee = 0.00
        else:
            if vt == 1:          # Motorcycle
                fee = 10 + (hrs - 1) * 5
            else:                # Personal Car
                fee = 30 + (hrs - 1) * 15
        print(f"Parking fee: {fee:.2f} THB")
        records.append((vt, hrs, fee))  # เก็บเฉพาะรายการที่ถูกต้อง

    # ถามว่าจะทำต่อไหม
    print("Do you want to continue? (y/n): ", end="")
    cont = input().strip().lower()
    print("------------------------------")
    if cont != "y":
        break

# สรุปรายการ
print("VT Hours Cost")
total = 0.0
for vt, hrs, fee in records:
    print(f"{vt} {hrs:.2f} {fee:.2f}")
    total += fee
print(f"Total {total:.2f} THB")