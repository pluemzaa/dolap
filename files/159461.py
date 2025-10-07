v = float(input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): "))
n = float(input ("Please enter the number of parking hours: "))
if v == 1:
    if n <= 0:    
        print("Please enter a valid number of parking hours")
    elif n > 0 and n < 1:
        print("Parking fee: 0.00 THB")
    elif n >= 1:
        p = 10 + (n-1) * 5
        print(f"Parking fee: {p:.2f} THB")
elif v == 2:
    if n <= 0 :   
        print("Please enter a valid number of parking hours")
    elif n > 0 and n < 1:
        print("Parking fee: 0.00 THB")
    elif n >= 1:
        p = 30 + (n-1) * 15
        print(f"Parking fee: {p:.2f} THB")
else:
    print("Invalid vehicle type")