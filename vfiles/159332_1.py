VH = (1,2)
T = int(input("Please enter vehicle type (1: Motocycle, 2: Personal Car):"))
H = float(input("Please enter the number of parking hours:"))

if T in VH:
    if T == 1:
        if H > 0:
            M = 10
            print(f"Parking fee: {M:.2f}")
        elif H > 1:
            H = H * 5
            M = 10 + H
            print(f"Parking fee: {M:.2f}")
        else:
            print("Please enter a valid number of parking hours")

    elif T == 2:
        if H > 0:
            M = 30
            print(f"Parking fee: {M:.2f}")
        elif H > 1:
            H = H * 15
            M = 30 + H
            print(f"Parking fee: {M:.2f}")
        else:
            print("Please enter a valid number of parking hours")

else:
    print("Invalid vehicle type")