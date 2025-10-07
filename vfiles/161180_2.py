total = 0.0
# mem = {'1':0,'2':0}

v_h_1 = 0
v_h_2 = 0
v_c_1 = 0
v_c_2 = 0


while True:
    veh_type = int(input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): "))
    hours = float(input("Please enter the number of parking hours: "))
    if hours > 0:
        if veh_type in [1,2]:
                if(hours >= 1):
                    if veh_type == 1:
                        fee = 10.0 + (5.0*(hours-1))
                        v_c_1 += fee
                        v_h_1 += hours
                    else:
                        fee = 30.0 + (15.0*(hours-1))
                        v_c_2 += fee
                        v_h_2 += hours
                else:
                    if veh_type == 1:
                        fee = 0.0
                        v_c_1 += fee
                        v_h_1 += hours
                    else:
                        fee = 0.0
                        v_c_2 += fee
                        v_h_2 += hours

                total += fee

                # mem.append((veh_type,hours,fee))
                print(f"Parking fee: {fee:.2f} THB")
        else:
            print("Invalid vehicle type")
    else:
        # print("Please enter a valid number of parking hours")
        print("Please enter a valid number of parking hours")

    check = input("Do you want to continue? (y/n): ")
    if check == 'n':
        print("------------------------------ ")
        print("VT Hours Cost")
        if v_h_1 > 0:
            print(f"1 {v_h_1:.2f} {v_c_1:.2f}")

        if v_h_2 > 0:
            print(f"2 {v_h_2:.2f} {v_c_2:.2f}")

            
        print(f"Total {total:.2f} THB")
        break
    
    else:
        print("------------------------------ ")