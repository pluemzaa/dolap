vc = input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): ")
hr = float(input("Please enter the number of parking hours: "))
if hr <= 0:
    print("Please enter a valid number of parking hours")
    exit()
if hr < 1:
    print("Parking fee: 0.00 THB")
    exit()
if vc == "1":
    price = 10 + (hr - 1) * 5
    print(f"Parking fee: {price:.2f} THB")
elif vc == "2":
    price = 30 + (hr - 1) * 15
    print(f"Parking fee: {price:.2f} THB")
else:
    print("Invalid vehicle type")