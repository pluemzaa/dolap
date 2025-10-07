veci = (int(input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): ")))
hoh = (float(input("Please enter the number of parking hours:")))
if veci not in [1,2]:
    print("Invalid vehicle type")
elif hoh <=0 :
    print("Please enter a valid number of parking hours")
else:
    if hoh < 1:
        fee = 0.00
    else:
        fiho = 1
        exhoh = hoh-1
        if veci == 1:
            fee = 10 + (exhoh*5)
        elif veci == 2:
            fee = 30 + (exhoh*15)
    print("Parking fee: ","%.2f"%fee,"THB")