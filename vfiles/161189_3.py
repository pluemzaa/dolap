records = []

while True:
    print("Please enter vehicle type (1: Motorcycle, 2: Personal Car): ", end="")
    vt_raw = input()
    print("Please enter the number of parking hours: ", end="")
    hrs_raw = input()

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

    if (not ok_type) or (vt not in [1, 2]):
        print("Invalid vehicle type")
    elif (not ok_hours) or (hrs <= 0):
        print("Please enter a valid number of parking hours")
    else:
        if hrs < 1:
            fee = 0.00
        elif vt == 1:
            fee = 10 + (hrs - 1) * 5
        else:
            fee = 30 + (hrs - 1) * 15

        # ใช้ฟอร์แมตมาตรฐาน -> 0.00
        print(f"Parking fee: {fee:.2f} THB")

        records.append((vt, hrs, fee))

    print("Do you want to continue? (y/n): ", end="")
    cont = input().strip().lower()
    print("------------------------------")
    if cont != "y":
        break

print("VT Hours Cost")
total = 0.0
for vt, hrs, fee in records:
    print(f"{vt} {hrs:.2f} {fee:.2f}")
    total += fee
print(f"Total {total:.2f} THB")