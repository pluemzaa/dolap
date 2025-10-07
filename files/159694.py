vtype = int(input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): "))
hours = float(input("Please enter the number of parking hours: "))
if hours <= 0:
    print("Please enter a valid number of parking hours")
elif vtype not in [1, 2]:
    print("Invalid vehicle type")
else:
    if hours < 1:
        fee = 0.00
    else:
        if vtype == 1:
            fee = 10 + (hours - 1) * 5
        else:
            fee = 30 + (hours - 1) * 15
    print(f"Parking fee: {fee:.2f} THB")