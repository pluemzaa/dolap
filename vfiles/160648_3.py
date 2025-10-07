VH = []

while True:
    V = int(input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): "))
    H = float(input("Please enter the number of parking hours: "))
    M = 0
    
    if H <= 0:
        print("Please enter a valid number of parking hours")
        break
    else:
        if V == 1:
            if 0 < H < 1:
                M = 0
                print(f"Parking fee: {M:.2f} THB")
            elif H >= 1:
                M = 10 + 5*(H-1)
                print(f"Parking fee: {M:.2f} THB")
        elif V == 2:
            if 0 < H < 1:
                M = 0
                print(f"Parking fee: {M:.2f} THB")
            elif H >= 1:
                M = 30 + 15*(H-1)
                print(f"Parking fee: {M:.2f} THB")
        else:
            print("Invalid vehicle type")
            cont = input("Do you want to continue? (y/n):")
            if cont == "y":
                print("------------------------------")
            elif cont == "n":
                print("------------------------------")
                break
            if H > 0:
                VH.append((V, H, M))
        cont = input("Do you want to continue? (y/n): ")
        print("------------------------------")
        if cont == "n":
            break
                
    print("VT Hours Cost")
    total = 0
    for V, H, M in VH:
        print(f"{V} {H:.2f} {M:.2f}")
        total += M
    print(f"Total {total}", "THB")