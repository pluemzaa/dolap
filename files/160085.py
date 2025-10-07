type = int(input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): "))
hours = float(input("Please enter the number of parking hours: "))

if hours >= 1 and type == 1 :
    fee = 10 + ((hours - 1) * 5)
    print(f"Parking fee: {fee:.2f} THB")
elif hours >= 1 and type == 2 :
    fee = 30 + ((hours - 1) * 15)
    print(f"Parking fee: {fee:.2f} THB")
else :
    if 0 < hours < 1 :
        print("Parking fee: 0.00 THB")
    elif hours <= 0 : 
        print("Please enter a valid number of parking hours")
    else:
        print("Invalid vehicle type")