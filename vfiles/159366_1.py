vh = int(input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): "))
ph = float(input("Please enter the number of parking hours: "))
price = 0
if vh <= 0:
    print("Please enter a valid number of parking hours")
elif vh==1:
    if ph < 1:
        price = 0
    if ph == 1:
        price = 10
    if vh > 1:
        price = 10+((vh-1)*5)
    print(f"Parking fee: {price:.2f} THB")

elif vh==1:
    if ph < 1:
        price = 0
    if ph == 1:
        price = 30
    if ph > 1:
        price = 30+((vh-1)*15)
    print(f"Parking fee: {price:.2f} THB")
else:
    print("Invalid vehicle type")