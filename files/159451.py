n1 = int(input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): "))#type
n2 = float(input("Please enter the number of parking hours: "))#time

if n1 == 1 or n1 == 2:
    if n2 > 0:
        if n1 == 1:
            R = (n2-1) *5 + 10
            R1 = 10
            if n2 < 1:
                print("Parking fee: 0.00 THB")
            elif n2 == 1:
                print(f"Parking fee: {R1:.2f} THB")
            elif n2 > 1:
                print(f"Parking fee: {R:.2f} THB")

        elif n1 == 2:
            RE = (n2-1) *15 + 30
            RE1 = 30
            if n2 < 1:
                print("Parking fee: 0.00 THB")
            elif n2 == 1:
                print(f"Parking fee: {RE1:.2f} THB")
            elif n2 > 1:
                print(f"Parking fee: {RE:.2f} THB")
    else:
        print("Please enter a valid number of parking hours")
else:
    print("Invalid vehicle type")