w = int(input("Please enter vehicle type (1: Motorcycle, 2: Personal Car):"))
s = float(input("Please enter the number of parking hours:"))
a = 0

if w>2:
    print("Invalid vehicle type")
elif s<=0:
    print("Please enter a valid number of parking hours")
elif s>0 and s<1:
    print("Parking fee: 0.00 THB")
else:
    if w==1:
        a = ((s-1)*5)+10
        print(f"Parking fee:{a:.2f} THB")
    else:
        a = ((s-1)*15)+30
        print(f"Parking fee:{a:.2f} THB")