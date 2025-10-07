t = int(input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): "))
pt = float(input("Please enter the number of parking hours: "))
price = 0
if t == 1 :
  if pt > 0:
    if pt <1 :
      price = 0
    elif pt == 1:
      price = 10
    elif pt > 1:
      price = 10
      price = price+((pt-1)*5)
    print(f"Parking fee: {price:.2f} THB") 
  else :
    print("Please enter a valid number of parking hours")
elif t == 2 :
  if pt > 0:
    if pt <1 :
      price = 0
    elif pt == 1:
      price = 30
    elif pt > 1:
      price = 30
      price = price+((pt-1)*15)
    print(f"Parking fee: {price:.2f} THB")
  else :
    print("Please enter a valid number of parking hours") 
else :
  print("Invalid vehicle type")