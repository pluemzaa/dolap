records = []
total_fee = 0

while True:
    v = int(input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): "))
    h = float(input("Please enter the number of parking hours: "))

    if v == 1 or v == 2:
        if h > 0:
            if h < 1:
                fee = 0
            elif v == 1:
                fee = 10 + (h - 1) * 5
            elif v == 2:
                fee = 30 + (h - 1) * 15

            fee = round(fee, 2)
            print(f"Parking fee: {fee:05.2f} THB")

            records.append((v, h, fee))
            total_fee += fee
        else:
            print("Please enter a valid number of parking hours")
    else:
        print("Invalid vehicle type")

    gg = input("Do you want to continue? (y/n): ")
    print("------------------------------")
    if gg != 'y':
        break

print("VT Hours Cost")
for i in range(len(records)):
    vtype, hours, cost = records[i]
    if i == len(records) - 1:
        print(f"{vtype} {hours:.2f} {cost:.2f}\nTotal {total_fee:.2f} THB")
    else:
        print(f"{vtype} {hours:.2f} {cost:.2f}")