import math
def round_down_half(x):
    return math.floor(x * 2) / 2
vh = int(input("Please enter vehicle type (1: Motorcycle, 2: Personal Car):"))
ph = float(input("Please enter the number of parking hours: "))
price = 0
if ph <= 0:
    print("Please enter a valid number of parking hours")
elif vh == 1:
    if ph <= 1:
        price = 0
    else:
        price = ph * 6.5
        price = round_down_half(price)
    print(f"Parking fee: {price:.2f} THB")
elif vh == 2:
    if ph <= 1:
        price = 30
    else:
        price = 30 + (ph - 1) * 15
    print(f"Parking fee: {price:.2f} THB")
else:
    print("Invalid vehicle type")