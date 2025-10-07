car = int(input("Please enter vehicle type (1: Motorcycle, 2: Personal Car):"))
hour = float(input("Please enter the number of parking hours:"))

if car == 1 :
    if hour < 1 :
        price = 0.00
    elif hour == 1 :
        price = 10 
    else :
        price = ((hour-1) * 5) +10
elif car == 2 :
    if hour < 1 :
        price = 0.00 
    elif hour == 1:
        price = 30
    else :
        price =  ((hour-1) * 15) +30
else :
    print("Invalid vehicle type")

if hour <= 0 :
    print("Please enter a valid number of parking hours")

if car == 1 and hour > 0 :
    print(f"Parking fee: {price:.2f} THB")

if car == 2 and hour > 0 :
    print(f"Parking fee: {price:.2f} THB")