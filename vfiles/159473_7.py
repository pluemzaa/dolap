Vc = float(input("Please enter vehicle type (1: Motorcycle, 2: Personal Car):"))
num = float(input("Please enter the number of parking hours:"))

if Vc == 1:
    if num <= 0:
        print("Please enter a valid number of parking hours")
    elif num > 0 and num < 1:
        print("Parking fee: 0.00 THB")
    elif num >= 1:
        x = 10 + (num - 1) * 5
        print(f"Parking fee:{x: .2f} THB")
elif Vc == 2:
    if num <= 0:
        print("Please enter a valid number of parking hours")
    elif num > 0 and num < 1:
        print("Parking fee: 0.00 THB")
    elif num >= 1:
        x = 30 + (num - 1) * 15
        print(f"Parking fee:{x:.2f} THB")
else:
    print("Invalid vehicle type")