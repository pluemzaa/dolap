vt = int(input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): "))
ph = float(input("Please enter the number of parking hours: "))
if ph <= 0:
    print("Please enter a valid number of parking hours")
else:
  if vt == 1:
      if ph >= 1:
          pf = 10 + (ph - 1) * 5
      else:
          pf = 0
      print(f"Parking fee: {pf:.2f} THB")
  elif vt == 2:
      if ph >= 1:
          pf = 30 + (ph - 1) * 15
      else:
          pf = 0
      print(f"Parking fee: {pf:.2f} THB")
  else:
      print("Invalid vehicle type")