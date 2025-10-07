m = 10
c = 30

Vty = int(input("Please enter vehicle type (1: Motorcycle, 2: Personal Car):"))

hr = float(input("Please enter the number of parking hours:"))

if Vty == 1:
    if hr <= 0:
        print("Please enter a valid number of parking hours"))
    elif hr > 1 AND hr < 1:
        print(f"Parking fee:{(10 + ((hr-1) * 5)): .2f} THB")
    elif hr <= 0:
        print("Parking fee: 0.00 THB")
elif Vty == 2:
    if hr <= 0:
        print("Please enter a valid number of parking hours"))
    elif hr > 1 AND hr < 1:
        print(f"Parking fee:{(30 + ((hr-1) * 15)): .2f} THB")
    elif hr <= 0:
        print("Parking fee: 0.00 THB")
else:
    print("Invalid vehicle type")