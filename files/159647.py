car = int(input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): "))
hour = float(input("Please enter the number of parking hours: "))
if car <= 0 or car >= 3 :
    print("Invalid vehicle type")
if car == 1 :
    if hour < 0 :
        print("Please enter a valid number of parking hours")
    if hour >= 0 and hour < 1:
        z = 0
    if hour >= 1 and hour < 2:
        z = 10
    if hour >= 2 :
        z = 10 +((hour-1)*5)
if car == 2 :
    if hour < 0 :
        print("Please enter a valid number of parking hours")
    if hour >= 0 and hour < 1:
        z = 0
    if hour >= 1 and hour <2:
        z = 30
    if hour >= 2 :
        z = 30 + ((hour-1)*15)
print(f"Parking fee: {z: .2f}  THB")