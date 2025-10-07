VT_list = []
Hours_list = []
Cost_list = []

while True:
    Vehicle = float(input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): "))
    Hours = float(input("Please enter the number of parking hours: "))
    
    if Vehicle not in [1, 2]:
        print("Invalid vehicle type")
        break
    elif Hours <= 0:
        print("Please enter a valid number of parking hours")
        break
    elif Hours < 1:
        fee = 0.00
        print("Parking fee: 00.00 THB")
        VT_list.append(int(Vehicle))
        Hours_list.append(Hours)
        Cost_list.append(fee)
    elif Vehicle == 1:
        PriceMotorcycle = 10 + (Hours - 1) * 5
        print("Parking fee: %.2f THB" % PriceMotorcycle)
        VT_list.append(int(Vehicle))
        Hours_list.append(Hours)
        Cost_list.append(PriceMotorcycle)
    elif Vehicle == 2:
        PriceMotorPersonalcar = 30 + (Hours - 1) * 15
        print("Parking fee: %.2f THB" % PriceMotorPersonalcar)
        VT_list.append(int(Vehicle))
        Hours_list.append(Hours)
        Cost_list.append(PriceMotorPersonalcar)
    
    continue_choice = input("Do you want to continue? (y/n): ")
    print("------------------------------")
    
    if continue_choice != 'y':
        break

# แสดงสรุปผล
if VT_list:
    print("VT Hours Cost")
    total = 0
    for i in range(len(VT_list)):
        print("%d %.2f %.2f" % (VT_list[i], Hours_list[i], Cost_list[i]))
        total += Cost_list[i]
    print("Total %.2f THB" % total)