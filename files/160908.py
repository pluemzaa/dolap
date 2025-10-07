total_fee = 0
summary = []

while True:
    try:
        v = int(input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): "))
        h = float(input("Please enter the number of parking hours: "))
    except ValueError:
        print("Invalid input")
        cont = input("Do you want to continue? (y/n): ").lower()
        print("------------------------------")
        if cont != 'y':
            break
        continue

    if v not in [1, 2]:
        print("Invalid vehicle type")
        cont = input("Do you want to continue? (y/n): ").lower()
        print("------------------------------")
        if cont != 'y':
            break
        continue

    if h <= 0:
        print("Please enter a valid number of parking hours")
        cont = input("Do you want to continue? (y/n): ").lower()
        print("------------------------------")
        if cont != 'y':
            break
        continue

    if h < 1:
        fee = 0
    elif v == 1:
        fee = 10 + (h - 1) * 5
    elif v == 2:
        fee = 30 + (h - 1) * 15

    print(f"Parking fee: {fee:.2f} THB")
    total_fee += fee
    summary.append((v, h, fee))

    cont = input("Do you want to continue? (y/n): ").lower()
    print("------------------------------")
    if cont != 'y':
        break

print("VT Hours Cost")
for s in summary:
    print(f"{s[0]} {s[1]:.2f} {s[2]:.2f}")
print(f"Total {total_fee:.2f} THB")