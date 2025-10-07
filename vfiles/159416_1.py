vehicle = int(input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): "))
hours = float(input("Please enter the number of parking hours: "))
if hours <= 0:
    print("Please enter a valid number of parking hours")
elif vehicle == 1:
    if hours < 1:
        print("Parking fee: 0.00 THB")
    elif 1 <= hours < 2:
        fee = 10
        print(f"Parking fee: {fee:.2f}","THB")
    else:
        fee = 10 + 5*(hours-1)
        print(f"Parking fee: {fee:.2f}","THB")
elif vehicle == 2:
    if hours < 1:
        print("Parking fee: 0.00 THB")
    elif 1 <= hours < 2:
        fee = 30
        print(f"Parking fee: {fee:.2f}","THB")
    else:
        fee = 30 + 15*(hours-1)
        print(f"Parking fee: {fee:.2f}","THB")
else:
    print("Invalid vehicle type")