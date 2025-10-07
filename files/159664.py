vehicle = input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): ")
parking = float(input("Please enter the number of parking hours: "))
if  parking <= 0 :
    print("Please enter a valid number of parking hours")
elif parking < 1 :
    total = 0
    h = parking *0
    print(f"Parking fee: {h :.2f} THB")

elif parking < 1 :
    total = 0 
    h = parking -0
    h2 = h * 0
    print(f"Parking fee: {h2:.2f} THB")
elif vehicle == "1" : 
    total = 10 
    h = parking - 1
    h2 = h * 5
    h3 = h2 + total
    print(f"Parking fee: {h3:.2f} THB")
elif vehicle == "2" :
    total = 30 
    h = parking - 1
    h2 = h * 15
    h3 = h2 + total
    print(f"Parking fee: {h3:.2f} THB")
else:
    vehicle <= "3" 
    print("Invalid vehicle type")