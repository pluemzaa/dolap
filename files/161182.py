import math

money1Log = 0
money2Log = 0
duration1Log = 0
duration2Log = 0

while True:
    vType = input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): ").strip()

    if vType not in ["1", "2"]:
        print("Invalid vehicle type")
        continue

    try:
        duraTime = float(input("Please enter the number of parking hours: ").strip())
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
        continue

    if duraTime <= 0:
        print("Please enter a valid number of parking hours greater than 0.")
        continue

    rounded_time = math.ceil(duraTime)

    if vType == "1":
        fhour = 10
        nhour = 5
    else:
        fhour = 30
        nhour = 15

    if rounded_time > 1:
        fee = fhour + (rounded_time - 1) * nhour
    else:
        fee = fhour

    print(f"Parking fee: {fee:.2f} THB")

    if vType == "1":
        money1Log += fee
        duration1Log += rounded_time  
    else:
        money2Log += fee
        duration2Log += rounded_time  

    con = input("Do you want to continue? (y/n): ").strip().lower()
    print("------------------------------")
    if con == "n":
        break

print("VT Hours Cost")

if duration1Log > 0 or money1Log > 0:
    print(f"1 {duration1Log:.2f} {money1Log:.2f}")

if duration2Log > 0 or money2Log > 0:
    print(f"2 {duration2Log:.2f} {money2Log:.2f}")

print(f"Total {(money1Log + money2Log):.2f} THB")