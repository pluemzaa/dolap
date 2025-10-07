records = []
while True:
    vehicle = int(input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): "))
    hour = float(input("Please enter the number of parking hours: "))

    if vehicle != 1 and vehicle != 2:
        print("Invalid vehicle type")
    elif hour <= 0:
        print("Please enter a valid number of parking hours")
    else:
        if hour < 1:
            fee = 0.00
        elif vehicle == 1:
            fee = 10 + (hour - 1) * 5
        else:
            fee = 30 + (hour - 1) * 15
        print("Parking fee: %.2f THB" % fee)
        records.append((vehicle, hour, fee))

    cont = input("Do you want to continue? (y/n): ").lower()
    print("------------------------------")
    if cont != "y":
        break

print("VT Hours Cost")
total = 0
for v, h, f in records:
    print("%d %.2f %.2f" % (v, h, f))
    total += f
print("Total %.2f THB" % total)