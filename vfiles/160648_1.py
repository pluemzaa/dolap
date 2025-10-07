VH = (1, 2)

while True:
    V = int(input("Please enter vehicle type (1: Motorcycle, 2: Personal Car):"))
    H = float(input("Please enter the number of parking hours:"))
    
    if V == 1:
        if H > 0:
            if 0 < H < 1:
                M1 = 0
                print(f"Parking fee: {M1:.2f}", "THB" )
            elif H > 1:
                M1 = 10 + 5*(H-1)
                print(f"Parking fee: {M1:.2f}", "THB" )
            
        else:
            print("Please enter a valid number of parking hours")
            break
            
        cont = input("Do you want to continue? (y/n):")
        if cont == "y":
            print("------------------------------")
        elif cont == "n":
            print("------------------------------")
            break
    
    elif V == 2:
        if H > 0:
            if 0 < H < 1:
                M2 = 0
                print(f"Parking fee: {M2:.2f}", "THB" )
            elif H > 1:
                M2 = 30 + 15*(H-1)
                print(f"Parking fee: {M2:.2f}", "THB" )
            
        else:
            print("Please enter a valid number of parking hours")
            break
            
        cont = input("Do you want to continue? (y/n):")
        if cont == "y":
            print("------------------------------")
        elif cont == "n":
            print("------------------------------")
            break

else:
    print("Invalid vehicle type")

total = M1 + M2

print("VT Hours Cost")
print(V, H, M1)
print(V, H, M2)
print(f"Total {total}", "THB")