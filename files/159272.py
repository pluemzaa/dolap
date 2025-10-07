a = input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): ")
b = float(input("Please enter the number of parking hours: "))

if a == "1" or a == "2":
    if b > 0:
        if b >= 1:
            if a == "1":
                c = 10 + ((b-1)*5)
            else:
                c = 30 + ((b-1)*15)
        else:
            c = 0
        print(f"Parking fee: {c:.2f} THB")
    else:
        print("Please enter a valid number of parking hours")
else:
    print("Invalid vehicle type")