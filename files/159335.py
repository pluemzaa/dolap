vt = int(input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): "))
h = float(input("Please enter the number of parking hours: "))
price = 0

if h <= 0:
    print("Please enter a valid number of parking hours")

elif vt == 1:
    if h < 1:
        price = 0
    if h == 1:
        price = 10
    if h > 1:
        price = 10+((h-1)*5)
    print(f"Parking fee: {price:.2f} THB")

elif vt == 2:
    if h < 1:
        price = 0
    if h == 1:
        price = 30
    if h > 1:
        price = 30+((h-1)*15)
    print(f"Parking fee: {price:.2f} THB")

else:
    print("Invalid vehicle type")