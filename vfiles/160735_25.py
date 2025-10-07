m_cost = 0.00 
m_hour = 0.00 
c_cost = 0.00
c_hour = 0.00    
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
            m_cost = m_cost + cost
            m_hour = m_hour + hour
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
            c_cost = c_cost + cost
            c_hour = c_hour + hour
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
if m_hour > 0 :
    print(f"1 {m_hour : .2f} {m_cost : .2f}")
if c_hour > 0 :
    print(f"2 {c_hour : .2f} {c_cost : .2f}")
total = m_cost + c_cost
print(f"Total {total : .2f} THB")