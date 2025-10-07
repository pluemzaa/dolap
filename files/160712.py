records = []
total = 0.0

while True:
    try:
        vt = int(input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): "))
    except ValueError:
        print("Invalid vehicle type")
        break

    if vt not in [1, 2]:
        print("Invalid vehicle type")
        break

    try:
        hrs = float(input("Please enter the number of parking hours: "))
    except ValueError:
        print("Please enter a valid number of parking hours")
        break

    if hrs <= 0:
        print("Please enter a valid number of parking hours")
        break

    # คำนวณค่าจอด
    if hrs < 1:
        fee = 0.00
    else:
        if vt == 1:
            fee = 10 + (hrs - 1) * 5
        else:
            fee = 30 + (hrs - 1) * 15

    print(f"Parking fee: {fee:.2f} THB")
    records.append((vt, hrs, fee))
    total += fee

    cont = input("Do you want to continue? (y/n): ").strip().lower()
    print("------------------------------")
    if cont != 'y':
        break

# สรุปผลลัพธ์
if records:
    print("VT Hours Cost")
    for vt, hrs, fee in records:
        print(f"{vt} {hrs:.2f} {fee:.2f}")
    print(f"Total {total:.2f} THB")