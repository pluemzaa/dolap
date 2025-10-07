v = input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): ")
h = float(input("Please enter the number of parking hours: "))
x = 0.0

if h > 0 and v in ["1", "2"]:
    if v == "1":
        if h < 1:
            x = 0
        elif h >= 1:
            x = 10 + (h - 1) * 5
    elif v == "2":
        if h < 1:
            x = 0
        elif h >= 1:
             x = 30 + (h - 1) * 15
    print(f"Parking fee: {x:.2f} THB")
elif h <= 0:
    print("Please enter a valid number of parking hours")
else:
    print("Invalid vehicle type")