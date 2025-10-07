total_fee = 0.0
summary = ""
first = True

while True:
    print("Please enter vehicle type (1: Motorcycle, 2: Personal Car): ", end="")
    vehicle = input().strip()
    if vehicle != "1" and vehicle != "2":
        print("Invalid vehicle type")
        break

    print("Please enter the number of parking hours: ", end="")
    try:
        hours = float(input())
    except:
        print("Please enter a valid number of parking hours")
        break

    if hours <= 0:
        print("Please enter a valid number of parking hours")
        break

    if hours < 1:
        fee = 0.00
    elif vehicle == "1":
        fee = 10 + (hours-1)*5
    else: # vehicle == "2"
        fee = 30 + (hours-1)*15

    print(f"Parking fee: {fee:.2f} THB")

    # สะสมรายการใน summary
    if first:
        summary = "VT Hours Cost\n"
        first = False
    summary += f"{vehicle} {hours:.2f} {fee:.2f}\n"
    total_fee = total_fee + fee

    print("Do you want to continue? (y/n): ", end="")
    cont = input().strip().lower()
    print("------------------------------ ( copy ไปเลย)")
    if cont != "y":
        break

if summary != "":
    print(summary + f"Total {total_fee:.2f} THB")