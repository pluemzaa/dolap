while True:

 car = input("Please enter vehicle type (1: Motorcycle, 2: Personal Car):")


 ho = float(input("Please enter the number of parking hours: "))

 if ho < 1 :
    price = 0.00
    print("Parking fee: ",price," THB")
    
 elif car == 1 :
    if ho <=1 :
        price=10
    else:
        price = 10 + (ho - 1)*5
    print("Parking fee: ",price," THB")
 elif car == 2 :
    if ho <=1 :
        price=30
    else:
        price = 30+ (ho - 1)*15
    print("Parking fee: ",price," THB")
    
 else:
  print("Invalid vehicle type")
  
  Continue = input("Do you want to continue? (y/n): ")
 if Continue == "n" :
     break