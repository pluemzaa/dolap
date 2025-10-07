parked = [
    [1,0,0],  # Motorcycle
    [2,0,0]  # Personal Car
]
error = False

while True:
    _type = int(input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): "))
    hours = float(input("Please enter the number of parking hours: "))
    if hours > 0:
        if _type == 1: ## Motorcycle
            fee = 0
            if hours < 1:
                fee = 0
            else :
                fee = 10+((hours-1) * 5)
            print(f"Parking fee: {fee:.2f} THB")
            ##parked.append([_type,hours,fee])
            parked[0][1] += hours
            parked[0][2] += fee
        
        elif _type == 2: ## Personal Car
            fee = 0
            if hours < 1:
                fee = 0
            else :
                fee = 30+((hours-1) * 15)
                
            print(f"Parking fee: {fee:.2f} THB")
            #parked.append([_type,hours,fee])
            parked[1][1] += hours
            parked[1][2] += fee

        else :
            print("Invalid vehicle type")
    else :
        
        print("Please enter a valid number of parking hours")
        
    
    _continue = input("Do you want to continue? (y/n): ")
    if _continue == "n":
        print("------------------------------")
        break
    elif _continue == "y":
        print("------------------------------")
        pass
   
    

print("VT Hours Cost")
total = 0

for i in range(len(parked)):
    v = parked[i]
    if v[1] > 0:
        print(f"{v[0]} {v[1]:.2f} {v[2]:.2f}")
    total += v[2]
print(f"Total {total:.2f} THB")