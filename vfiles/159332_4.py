VH = (1,2)
V = int(input("Please enter vehicle type (1: Motorcycle, 2: Personal Car):"))
H = float(input("Please enter the number of parking hours:"))


if V in VH:
    if V == 1:
        if H > 0:
            if 0 < H <= 1:
                M = 10
                print(f"Parking fee: {M:.2f}", "THB" )
            elif H > 1:
                M = 10 + 5*(H-1)
                print(f"Parking fee: {M:.2f}", "THB" )
        else:
            print("Please enter a valid number of parking hours")
    elif V == 2:
        if H > 0:
            if 0 < H <= 1:
                M = 30
                print(f"Parking fee: {M:.2f}", "THB" )
            elif H > 1:
                M = 30 + 15*(H-1)
                print(f"Parking fee: {M:.2f}", "THB" )
        else:
            print("Please enter a valid number of parking hours")
else:
    print("Invalid vehicle type")