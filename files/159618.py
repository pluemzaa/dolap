Motorcycle = 1
Car = 2
a = int(input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): "))
b = float(input("Please enter the number of parking hours: "))
price = 0
if b < 0:
    print("Please enter a valid number of parking hours")
if a == 1:
    if b < 1:
        print(f"Parking fee: {price:.2f} THB")
    elif b == 1:
        print(f"Parking fee: {price+10:.2f} THB")       
    elif b >= 1:
        print(f"Parking fee: {price+10+(int(b)-1)*5:.2f} THB")
if a == 2:
    if b < 1:
        print(f"Parking fee: {price:.2f} THB")
    elif b == 1:
        print(f"Parking fee: {price+30:.2f} THB")       
    elif b >= 1:
        print(f"Parking fee: {price+30+(int(b)-1)*15:.2f} THB")

else:
    print("Invalid vehicle type")