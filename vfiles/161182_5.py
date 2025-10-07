money1Log = 0
money2Log = 0
duration1Log = 0
duration2Log = 0

while True:
    vType = input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): ")

    if vType not in ["1", "2"]:
        print("Invalid vehicle type")
        continue

    try:
        duraTime = float(input("Please enter the number of parking hours: "))
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
        continue

    if duraTime <= 0:
        print("Please enter a valid number of parking hours greater than 0.")
        continue

    if vType == "1":
        fhour = 10
        nhour = 5
    else:
        fhour = 30
        nhour = 15

    if duraTime > 1:
        fee = (duraTime - 1) * nhour + fhour
    else:
        fee = duraTime * fhour

    print(f"Parking fee: {fee:.2f} THB")

    if vType == "1":
        money1Log += fee
        duration1Log += duraTime
    else:
        money2Log += fee
        duration2Log += duraTime

    con = input("Do you want to continue? (y/n): ")
    print("------------------------------")
    if con.lower() == "n":
        break

print("VT Hours Cost")

if duration1Log > 0 or money1Log > 0:
    print(f"1 {duration1Log:.2f} {money1Log:.2f}")

if duration2Log > 0 or money2Log > 0:
    print(f"2 {duration2Log:.2f} {money2Log:.2f}")

print(f"Total {(money1Log + money2Log):.2f} THB")