Total_PersonalCar_price = 0
Total_Motorcycle_price = 0
Total_Motorcycle_Time = 0
Total_PersonalCar_Time = 0
while True:
    s = float(input("Please enter vehicle type (1: Motorcycle, 2: PersonalCar): "))
    Time = float(input("Please enter the number of parking hours: "))
 

    if s==1 :
        if Time > 0:
            if Time < 1 :
                Motorcycle_price = 0 * Time
                print(f"Parking fee: {Motorcycle_price:.2f} THB")
            elif Time == 1:
                Motorcycle_price = 10 * Time
                print(f"Parking fee: {Motorcycle_price:.2f} THB")
            else:
                Motorcycle_price =10+(Time-1) * 5
                print(f"Parking fee: {Motorcycle_price:.2f} THB")
            Total_Motorcycle_price = Total_Motorcycle_price + Motorcycle_price 
            Total_Motorcycle_Time = Total_Motorcycle_Time + Time
        else:
            print("Please enter a valid number of parking hours")

    elif s==2 :
        if Time > 0:
            if Time < 1 :
                PersonalCar_price = 0 * Time
                print(f"Parking fee: {PersonalCar_price:.2f} THB")
            elif Time == 1:
                PersonalCar_price = 30 * Time
                print(f"Parking fee: {PersonalCar_price:.2f} THB")
            else:
                PersonalCar_price = 30 + (Time-1) * 15
                print(f"Parking fee: {PersonalCar_price:.2f} THB")
            Total_PersonalCar_price = Total_PersonalCar_price + PersonalCar_price
            Total_PersonalCar_Time = Total_PersonalCar_Time + Time
        else:
            print("Please enter a valid number of parking hours")
    else :
        print("Invalid menu")

    con = input("Do you want to continue? (y/n):")
    print('------------------------------ ( copy ไปเลย)')
    if con=='n':
        print('------------------------------ ( copy ไปเลย)')
        break

print('VT Hours Cost')
print(1,f' {Total_Motorcycle_Time:.2f} {Total_Motorcycle_price:.2f}')
print(2,f' {Total_PersonalCar_Time:.2f} {Total_PersonalCar_price:.2f}')
print(f"Total : {Total_PersonalCar_price + Total_Motorcycle_price: .2f} THB")