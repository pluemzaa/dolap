cycle = 0
cycle_time = 0
car = 0
car_time = 0
while True:
    vehcle = int(input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): "))
    time = float(input("Please enter the number of parking hours: "))

    first_time = 10
    after_time = 5
    if vehcle ==2:
        first_time = 30
        after_time = 15
    
    if time <=0.5:
        parking_free = 0
    elif time <=1:
        parking_free = first_time
    else:
        parking_free = first_time + (time-1) * after_time   
    if vehcle !=1 and vehcle !=2:
        print("Invalid vehicle type")     
    elif time <0:
        print("Please enter a valid number of parking hours")  
    else:
        print(f"Parking fee: {parking_free:05.2f} THB")
        if vehcle ==1:
            cycle = parking_free
            cycle_time = cycle_time+time
        if vehcle == 2:
            car = parking_free
            car_time = car_time+time 
    continue_p = input("Do you want to continue? (y/n): ")
    print("------------------------------")
    if continue_p == "n" :
        break                 
print("VT Hours Cost") 
if cycle_time > 0 or cycle :
    print(f"1 {cycle_time:.2f} {cycle:.2f}") 
if car_time > 0 or car :        
    print(f"2 {car_time:.2f} {car:.2f}")  
print(f"Total {(cycle+car):.2f} THB")