motercost = 0.00 
moterhour = 0.00 
carcost = 0.00
carhour = 0.00    
while True: 
    cost = 0
    veh = int(input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): "))
    hour = float(input("Please enter the number of parking hours: "))
    if veh == 1 :
        if hour > 0 : 
            if hour < 1 :               
                cost = 0
                print(f"Parking fee: {cost : .2f} THB")
            else :
                cost = 10 + ((hour - 1) * 5 )
                print(f"Parking fee: {cost : .2f} THB")
            motercost = motercost + cost
            moterhour = moterhour + hour
        else :
            print("Please enter a valid number of parking hours")
        

    elif veh == 2 :
        if hour > 0 : 
            if hour < 1 :
                cost = 0
                print(f"Parking fee: {cost : .2f} THB")
            else :
                cost = 30 + ((hour - 1) * 15)
                print(f"Parking fee: {cost : .2f} THB")
            carcost = carcost + cost
            carhour = carhour + hour
        else :
            print("Please enter a valid number of parking hours")
        

    else :
        print("Invalid vehicle type")
        
    con = input("Do you want to continue? (y/n): ")
    print("------------------------------")
    if con == "y" :
        continue
    elif con == "n" :
        break
print ("VT Hours Cost")
total = 0
if moterhour > 0 :
    print(f"1 {moterhour : .2f} {motercost : .2f}")
if carhour > 0 :
    print(f"2 {carhour : .2f} {carcost : .2f}")
total = motercost + carcost
print(f"Total {total : .2f} THB")