x = int(input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): "))
r = float(input("Please enter the number of parking hours: "))


if x not in [1, 2]:
    print("Invalid vehicle type")
elif r <= 0:
    print("Please enter a valid number of parking hours")
else:
    if r < 1:
        fee = 0.0
    else:
        if x == 1: 
            fee = 10 + (r - 1) * 5
        elif x == 2: 
            fee = 30 + (r - 1) * 15
    print(f"Parking fee: {fee:.2f} THB")