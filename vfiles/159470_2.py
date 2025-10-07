ve = input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): ")
ho = float(input("Please enter the number of parking hours: "))

if  ve not in ['1','2']:
    print("Invalid vehicle type")
elif ho <= 0:
    print("Please enter a valid number of parking hours")
elif ho <= 1:
    print("Parking fee: 0.00 THB")
elif ve == '1':
    if ho > 1:
        fee = 10 + (ho - 1)*5
        print("Parking fee: %.2f THB" % fee)
elif ve == '2':
    if ho > 1 :        
        fee = 30 + (ho - 1)*15
        print("Parking fee: %.2f THB" % fee)