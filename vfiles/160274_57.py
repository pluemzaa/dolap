records = []
total_cost = 0

while True:
    c = int(input('Please enter vehicle type (1: Motorcycle, 2: Personal Car): '))
    h = float(input('Please enter the number of parking hours: '))

    if c not in (1, 2):
        print("Invalid vehicle type")
    elif h <= 0:
        print("Please enter a valid number of parking hours")
    else:
        if h < 1:
            fee = 0
        else:
            if c == 1:  # Motorcycle
                fee = 10 + (h - 1) * 5
            else:       # Personal Car
                fee = 30 + (h - 1) * 15

        print(f"Parking fee: {fee:05.2f} THB")
        records.append((c, h, fee))
        total_cost += fee

    cont = input("Do you want to continue? (y/n): ").lower()
    print("------------------------------")
    if cont == 'n':
        break

if records:
    print("VT Hours Cost")
    for r in records:
        print(f"{r[0]} {r[1]:.2f} {r[2]:05.2f}")
    print(f"Total {total_cost:05.2f} THB")