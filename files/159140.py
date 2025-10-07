vType = input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): ")
duraTime = float(input("Please enter the number of parking hours: "))

fhour = 10
nhour = 5

if duraTime < 1:
    fhour = 0
    nhour = 0

if vType == "2":
    fhour = 30
    nhour = 15

if (vType == "1" or vType == "2") and duraTime > 0:
    fee = (duraTime - 1) * nhour + (1 * fhour)

    print(f"Parking fee: {fee:.2f} THB")
    
elif not (vType == "1" or vType == "2"):
    print("Invalid vehicle type")
    
elif not duraTime > 0:
    print("Please enter a valid number of parking hours")