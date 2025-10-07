v = int(input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): "))
h = float(input("Please enter the number of parking hours: "))
if v > 2 or v < 0  :
    print ("Invalid vehicle type")
elif h <= 0 :
    print("Please enter a valid number of parking hours")
else :
    if h < 1  :     
        print("Parking fee: 0.00 THB")
    elif v == 1 and h >= 1:
        if h >= 1 :
            c = 5
            p = 10 + ((h-1)*c)
            print(f"Parking fee: {p:.2f} THB")
    elif v == 2 and h >= 1 :
        if h >= 1 :
            c = 15
            p = 30 + ((h-1)*c)
            print(f"Parking fee: {p:.2f} THB")