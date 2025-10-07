a = int(input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): "))
b = float(input("Please enter the number of parking hours: "))
p = 0

if a == 1:
      if b < 0 :
            print("Please enter a valid number of parking hours")
      elif b < 1:
            print(f"Parking fee: {p:.2f} THB")
      else:
            p = 5
            p = ((b - 1) * p) + 10
            print(f"Parking fee: {p:.2f} THB")
elif a == 2:
      if b < 0 :
            print("Please enter a valid number of parking hours")
      elif b < 1:
            print(f"Parking fee: {p:.2f} THB")
      else:
            p = 15
            p = ((b - 1) * p) + 30
            print(f"Parking fee: {p:.2f} THB")
else:
      print("Invalid vehicle type")