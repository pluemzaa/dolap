vtype = int(input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): "))
num = float(input("Please enter the number of parking hours: "))
if num <= 0:
    print("Please enter a valid number of parking hours")
elif vtype >= 3:
    print("Invalid vehicle type")
else:
    if vtype == 1 and num >= 1:
        fee = 10 +((num-1)*5)
        print(f"Parking fee: {fee:.2f} THB")
    elif vtype == 1 and num < 1:
        print("Parking fee: 0.00 THB")
    if vtype == 2 and num >= 1:
        fee = 30 +((num-1)*15)
        print(f"Parking fee: {fee:.2f} THB")
    elif vtype == 2 and num < 1:
        print("Parking fee: 0.00 THB")