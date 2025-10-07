MTT = 0  # Motorcycle Total Time
MTF = 0  # Motorcycle Total Fee
CTT = 0  # Car Total Time
CTF = 0  # Car Total Fee

while True:
    fee = 0
    try:
        vehi = int(input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): "))
    except ValueError:
        print("Invalid vehicle type")
        break

    if vehi not in [1, 2]:
        print("Invalid vehicle type")
        break

    try:
        time = float(input("Please enter the number of parking hours: "))
    except ValueError:
        print("Please enter a valid number of parking hours")
        break

    if time <= 0:
        print("Please enter a valid number of parking hours")
        break

    if time < 1:
        fee = 0
        print("Parking fee: 0.00 THB")
    elif vehi == 1:
        fee = 10 + (time - 1) * 5
        print(f"Parking fee: {fee:.2f} THB")
        MTT += time
        MTF += fee
    elif vehi == 2:
        fee = 30 + (time - 1) * 15
        print(f"Parking fee: {fee:.2f} THB")
        CTT += time
        CTF += fee

    cont = input("Do you want to continue? (y/n): ").lower()
    if cont == "n":
        print("------------------------------")
        print("VT Hours Cost")
        if MTT > 0:
            print(f"1 {MTT:.2f} {MTF:.2f}")
        if CTT > 0:
            print(f"2 {CTT:.2f} {CTF:.2f}")
        print(f"Total {MTF + CTF:.2f} THB")
        break
    else:
        print("------------------------------")