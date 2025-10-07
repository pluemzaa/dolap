m1 = 0
m2= 0

d1 = 0
d2 = 0

while True:
    vType = input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): ")
    duraTime = float(input("Please enter the number of parking hours: "))

    fh = 10
    nh = 5
    
    if vType == "2":
        fh = 30
        nh = 15

    if duraTime < 1:
        fh = 0
        nh = 0
        
    if (vType == "1" or vType == "2") and duraTime > 0:
        fee = (duraTime - 1) * nh + (1 * fh)

        print(f"Parking fee: {fee:.2f} THB")
        
        if vType == "1":
            m1 += fee
            d1 += duraTime
        else:
            m2 += fee
            d2 += duraTime
            
    elif not (vType == "1" or vType == "2"):
        print("Invalid vehicle type")
        
    elif  duraTime <= 0:
        print("Please enter a valid number of parking hours")
    
    cont = input("Do you want to continue? (y/n): ")
    
    print("------------------------------")
    
    if cont == "n":
        break

print("VT Hours Cost")
print(f"1 {d1:.2f} {m1:.2f}")
print(f"2 {d2:.2f} {m2:.2f}")
print(f"Total {(m1 + m2):.2f} THB")