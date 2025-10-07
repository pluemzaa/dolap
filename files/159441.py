v = int(input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): "))
h = float(input("Please enter the number of parking hours: "))
if v==1 or v==2:
    if h <= 0:
        print("Please enter a valid number of parking hours")
    elif h < 1:
        print("Parking fee: 0.00 THB")
    else:
        if v == 1 :
            fe = 10 + (h - 1) * 5
        elif v == 2:
            fe = 30 + (h - 1) * 15
        print(f"Parking fee: {fe:.2f} THB")
else:
   print("Invalid vehicle type")