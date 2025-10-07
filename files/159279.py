v = float(input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): "))
h = float(input("Please enter the number of parking hours: "))
u = 0
if h <= 0:
    print("Please enter a valid number of parking hours")        
elif v == 1:
    u = ((h - 1) * 5) + 10
    print(f"Parking fee: {u:.2f} THB")
elif v == 2:
    u = ((h - 1) * 15) + 30
    print(f"Parking fee: {u:.2f} THB")
else:
    print("Invalid vehicle type")