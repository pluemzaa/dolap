parking_data = []
while True:
    try:
        v_type = int(input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): "))
        h = float(input("Please enter the number of parking hours: "))

        if v_type not in [1, 2]:
            print("Invalid vehicle type")
        elif h <= 0:
            print("Please enter a valid number of parking hours")
        else:
            if h < 1:
                fee = 0.00
            elif v_type == 1:
                fee = 10 + (h - 1) * 5
            elif v_type == 2:
                fee = 30 + (h - 1) * 15

            print(f"Parking fee: {fee:.2f} THB")
            parking_data.append((v_type, h, fee))

    except ValueError:
        print("Invalid input")
    
    cont = input("Do you want to continue? (y/n): ")
    print("------------------------------")
    if cont != 'y':
        break

print("VT Hours Cost")
total = 0
for vt, hrs, cost in parking_data:
    print(f"{vt} {hrs:.2f} {cost:.2f}")
    total += cost
print(f"Total {total:.2f} THB")