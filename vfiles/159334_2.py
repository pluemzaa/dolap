v = int(input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): "))
h = float(input("Please enter the number of parking hours: "))
mo = 1
car = 2
if h > 0 :
    if h > 1 :
        if v == 1:
            print(f"Parking fee: {10 + ((h-1)*5):.2f} Baht")
        elif v == car:
            print(f"Parking fee: {30 + ((h-1)*15):.2f} Baht")
        else:
            print("Invalid vehicle type")
    else:
        print("Parking fee: 0.00 THB")
else:
    print("Please enter a valid number of parking hours")