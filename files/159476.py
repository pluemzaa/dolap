Moto = int(input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): "))
perso = float(input("Please enter the number of parking hours: "))

if Moto != 1 and Moto != 2:
    print("Invalid vehicle type")
elif perso <= 0:
    print("Please enter a valid number of parking hours")
elif perso < 1:
    print("Parking fee: 0.00 THB")
else:
    if Moto == 1:  
        fee = 10 + (perso - 1) * 5
    elif Moto == 2:  
        fee = 30 + (perso - 1) * 15
    print(f"Parking fee: {fee:.2f} THB")