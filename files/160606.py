money1Log = 0
money2Log = 0

duration1Log = 0
duration2Log = 0

while True:
    vType = input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): ")
    duraTime = float(input("Please enter the number of parking hours: "))

    fhour = 10
    nhour = 5
    
    if vType == "2":
        fhour = 30
        nhour = 15

    if duraTime < 1:
        fhour = 0
        nhour = 0
        
    if (vType == "1" or vType == "2") and duraTime > 0:
        fee = (duraTime - 1) * nhour + (1 * fhour)

        print(f"Parking fee: {fee:.2f} THB")
        
        if vType == "1":
            money1Log += fee
            duration1Log += duraTime
        else:
            money2Log += fee
            duration2Log += duraTime
            
    elif not (vType == "1" or vType == "2"):
        print("Invalid vehicle type")
        
    elif not duraTime > 0:
        print("Please enter a valid number of parking hours")
    
    con = input("Do you want to continue? (y/n): ")
    
    print("------------------------------")
    
    if con == "n":
        break

print("VT Hours Cost")

if duration1Log > 0 or money1Log > 0:
    print(f"1 {duration1Log:.2f} {money1Log:.2f}")
    
if duration2Log > 0 or money2Log > 0:
    print(f"2 {duration2Log:.2f} {money2Log:.2f}")
    
print(f"Total {(money1Log + money2Log):.2f} THB")