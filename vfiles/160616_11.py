records = []
total_fee = 0
while True:
    _vehicle = int(input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): "))
    _hours = float(input("Please enter the number of parking hours: "))
    if _vehicle not in [1, 2]:
        print("Invalid vehicle type")
    elif _hours <= 0:
        print("Please enter a valid number of parking hours")
    else:
        if _vehicle == 1:
            if _hours < 1:
                fee = 0.00
            else:
                fee = 10 + (_hours - 1) * 5
        elif _vehicle == 2:
            if _hours < 1:
                fee = 0.00
            else:
                fee = 30 + (_hours - 1) * 15
        print("Parking fee: %.2f THB" % fee)
        records.append((_vehicle, _hours, fee))
        total_fee += fee
    con = input("Do you want to continue? (y/n): ")
    print("------------------------------")
    if con == "n":
        break
print("VT Hours Cost")
for r in records:
    print(f"{r[0]} {r[1]:.2f} {r[2]:.2f}")
print("Total %.2f THB" % r[2])