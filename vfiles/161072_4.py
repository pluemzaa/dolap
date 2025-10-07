bikePrice = 0
bikeCount = 0
bikeparking = 0
carPrice = 0
carCount = 0
carparking = 0
price = 0
while True:
    choice = int(input("Please enter vehicle type (1: Motorcycle, 2: Personal Car):"))
    parking = float(input("Please enter the number of parking hours:"))
    #############################Bike
    if choice ==1: 
        # parking = float(input("Please enter the number of parking hours:"))
        if parking >= 1:
            bikeparking = parking
            bikePrice = (bikePrice + 10)+(parking*5)-5
            bikeCount = bikeCount + 1
            print(f"Parking fee: {bikePrice} THB")
        elif bikeparking < 1:
            bikeparking = parking
            bikeCount = bikeCount + 1
            print(f"Parking fee: {bikePrice} THB")
    #############################Car
    if choice ==2:
        # parking = float(input("Please enter the number of parking hours:"))
        if parking >= 1:
            carPrice = (carPrice + 30)+(parking*15)-15
            carCount = carCount + 1
            carparking = parking
            print(f"Parking fee: {carPrice} THB")
        elif parking < 1:
            carCount = carCount + 1
            carparking = parking
            print(f"Parking fee: {carPrice} THB")
    else:
        if choice > 2:
            print("Invalid vehicle type")
        if choice < 1:
            print("Invalid vehicle type")
        if parking < 0:
            print("Please enter a valid number of parking hours")
    con = input("Do you want to continue? (y/n):")
    if con=='n':
        break
print("VT Hours Cost")
print(bikeCount,bikeparking,bikePrice)
print(carCount,carparking,carPrice)
price = bikePrice + carPrice
print(f"Total {price} THB")