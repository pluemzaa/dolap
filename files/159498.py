t = input("Please enter vehicle type (1: Motorcycle,2: Personal Car): ")
h = float(input("Please enter the number of parking hours: "))

if t not in ["1", "2"]:
    print("Invalid vehicle type")
elif h <= 0:
    print("Please enter a valid number of parking hours")
else:
    if t == "1":
        if h <= 1:
            print("Parking fee: 0.00 THB")
        else:
            fee = 10 + (h - 1) * 5
            print(f"Parking fee: {fee:.2f} THB")
    elif t == "2":
        if h <= 1:
            print("Parking fee: 0.00 THB")
        else:
            fee = 30 + (h - 1) * 15
            print(f"Parking fee: {fee:.2f} THB")