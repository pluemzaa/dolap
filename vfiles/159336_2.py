x = input("Please enter vehicle type (1: Motorcycle, 2: Personal Car):")
y = float(input("Please enter the number of parking hours:"))
B = 0
if x == "1" :
    if y <= -1:
        print("Please enter a valid number of parking hours")
    elif y <= 0.5:
        print(f"Parking fee: {B:.2f} THB") 
    elif y <= 1:
        B=10+B
        print(f"Parking fee: {B:.2f} THB")
    elif y <= 2:
        B=15+B
        print(f"Parking fee: {B:.2f} THB")
    elif y <= 3:
        B=20+B
        print(f"Parking fee: {B:.2f} THB")
    elif y <= 4:
        B=25+B
        print(f"Parking fee: {B:.2f} THB")
    elif y <= 5:
        B=30+B
        print(f"Parking fee: {B:.2f} THB") 
    elif y <= 6:
        B=35+B
        print(f"Parking fee: {B:.2f} THB")
    elif y <= 7:
        B=40+B
        print(f"Parking fee: {B:.2f} THB")
    else:
        print("Please enter a valid number of parking hours")
elif x=="2" :
    ify <= -1 :
        print("Please enter a valid number of parking hours")
    elif y <= 0.5:
        print(f"Parking fee: {B:.2f} THB") 
    elif y <= 1:
        B=30+B
        print(f"Parking fee: {B:.2f} THB")
    elif y <= 2:
        B=45+B
        print(f"Parking fee: {B:.2f} THB")
    elif y <= 3:
        B=60+B
        print(f"Parking fee: {B:.2f} THB")
    elif y <= 4:
        B=75+B
        print(f"Parking fee: {B:.2f} THB")
    elif y <= 5:
        B=90+B
        print(f"Parking fee: {B:.2f} THB") 
    elif y <= 6:
        B=105+B
        print(f"Parking fee: {B:.2f} THB")
    elif y <= 7:
        B=120+B
        print(f"Parking fee: {B:.2f} THB")
    
else:
    print("Invalid vehicle type")  
#