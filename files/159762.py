x = int(input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): "))
y = float(input("Please enter the number of parking hours:"))
price = 0    
if x == 1:
    if y > 0:
      if y < 1 :
        price = 0
      elif y == 1:
        price = 10
      elif y > 1:
        price = 10
        price = price + (y - 1) * 5
      print(f"Parking fee:{price:.2f}" ,"THB")
    else: 
      print("Please enter a valid number of parking hours")
elif x == 2:
  if y > 0:
    if y <1 :
      price = 0
    elif y == 1:
      price = 30
    elif y > 1:
      price = 30
      price = price + (y - 1) * 15
    print(f"Parking fee:{price:.2f}" ,"THB")
  else:
    print("Please enter a valid number of parking hours")
else:
  print("Invalid vehicle type")