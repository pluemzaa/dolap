x = int(input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): "))
y = float(input("Please enter the number of parking hours: "))

if x not in [1, 2]:
    print("Invalid vehicle type")
elif y <= 0:
    print("Please enter a valid number of parking hours")
elif y < 1:
    print("Parking fee: 0.00 THB")       
else:
    if x == 1:
        if y == 1:
            fee = 10  
        else:
            fee = 10 + (y - 1) * 5  
    elif x == 2:
        if y == 1:
            fee = 30
        else:
            fee = 30 + (y - 1) * 15

print(f"Parking fee: {fee:.2f} THB")