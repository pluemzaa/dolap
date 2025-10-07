v = float(input(”Please enter vehicle type (1: Motorcycle, 2: Personal Car): “))
h = float(input(”Please enter the number of parking hours: “))
r = 0
if h <= 0:
    print(”Please enter a valid number of parking hours“)        
elif v == 1:
    r = ((h-1) * 5) + 10
    print(”Parking fee: %.2f THB“% (r))
elif v == 2:
    r = ((h-1) * 15) + 30
    print(”Parking fee: %.2f THB“% (r))
    
else:
    print(”Invalid vehicle type“)