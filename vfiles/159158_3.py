vt= float(input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): "))
h = float(input("Please enter the number of parking hours: "))
if vt==1:
    if h >= 1:
        price = 10
    elif h <= 2:
        price = 5
    else:
        price = 0
    price = price * h
    print(f"Parking fee: {price:.2f}")
elif vt== 2 :
    if h >= 1:
        price = 10
    elif h <= 2:
        price = 5
    else:
        price = 0
    price = price * h
    print(f"Parking fee: {price:.2f}")
else:
    print("Invalid vehicle type")