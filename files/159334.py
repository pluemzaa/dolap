v = int(input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): "))
h = float(input("Please enter the number of parking hours: "))
if h > 0 :
        if v == 1:
            if h < 1 and h > 0:
                print(f"Parking fee: {0:.2f} THB")
            else:
                print(f"Parking fee: {10 + ((h-1)*5):.2f} THB")
        elif v == 2:
            if h < 1 and h > 0:
                print(f"Parking fee: {0:.2f} THB")
            else:
                print(f"Parking fee: {30 + ((h-1)*15):.2f} THB")
        else:
             print("Invalid vehicle type")
    #else:
         #print(f"Parking fee: {0.00} THB")
else:
    print("Please enter a valid number of parking hours")