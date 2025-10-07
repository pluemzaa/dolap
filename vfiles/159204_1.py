v = input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): ")
h = float(input("Please enter the number of parking hours: "))

if h > 0 and v in ["1", "2"]:
    if v == "1":
        if h < 1:
            fee = 0
        elif h == 1:
            fee = 5
        elif h > 1:
            fee = 5 + (h*5)
    elif v == "2":
        if h < 1:
            fee = 0
        elif h == 1:
            fee = 30
        elif h > 1:
            fee = 30 + (h*15)
    print(f"Parking fee: {fee:.2f} THB")
elif h <= 0:
    print("Please enter a valid number of parking hours")
elif v not in ["1", "2"]:
    print("Invalid vehicle type")