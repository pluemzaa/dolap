v_type = input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): ")
hours = float(input("Please enter the number of parking hours: "))

if v_type != '1' and v_type != '2':
    print("Invalid vehicle type")
elif hours <= 0:
    print("Please enter a valid number of parking hours")
else:
    if hours < 1:
        fee = 0.0
    else:
        if v_type == '1':
            fee = 10 + (hours - 1) * 5
        else:
            fee = 30 + (hours - 1) * 15
    print(f"Parking fee: {fee:.2f} THB")