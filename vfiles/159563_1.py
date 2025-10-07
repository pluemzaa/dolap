ui = int(input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): "))
io = float(input("Please enter the number of parking hours: "))

if ui == 1 or ui == 2:
    if io <= 0:
        if 0 < io < 1:
            print("Parking fee: 0.00 THB")
            if ui == 1:
                re = io - 1
                total = 10
                ji = re * 5
                uall = ji + total
                print(f"Parking fee: {uall:.2f} THB")
            elif ui == 2:
                re = io - 1
                total = 30
                ji = re * 15
                uall = ji + total
                print(f"Parking fee: {uall:.2f} THB")
    else:
        print("Please enter a valid number of parking hours")
else:
    print("Invalid vehicle type")