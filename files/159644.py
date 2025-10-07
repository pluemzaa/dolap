type = int(input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): "))
park_time = float(input("Please enter the number of parking hours: "))
fee = 0

if type == 1 :
    if park_time < 0:
     print("Please enter a valid number of parking hours")
    elif park_time < 1 :
        fee = 0
        print(f"Parking fee: {fee:.2f} THB")
    elif park_time <= 1 :
        fee = 10*park_time ; 
        print(f"Parking fee: {fee:.2f} THB")
    elif park_time > 1:
        fee = (5 * (park_time-1)) + 10
        print(f"Parking fee: {fee:.2f} THB")
    
if type == 2 :
    if park_time < 0:
     print("Please enter a valid number of parking hours")
    elif park_time < 1 :
        fee = 0
        print(f"Parking fee: {fee:.2f} THB")
    elif park_time<= 1 :
        fee = 30 * park_time ; 
        print(f"Parking fee: {fee:.2f} THB")
    elif park_time > 1:
            fee = (15 * (park_time-1) + 30);
            print (f"Parking fee: {fee:.2f} THB")
elif type > 2 : 
    print("Invalid vehicle type")