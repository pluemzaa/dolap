summary = []
v while True:
vehicle_type_input = input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): ")
if not vehicle_type_input.isdigit():
print("Invalid vehicle type")
continue
vehicle_type = int(vehicle_type_input)
く
く
く
く
if vehicle_type != 1 and vehicle_type != 2:
print("Invalid vehicle type")
continue
try:
hours = float (input("Please enter the number of parking hours: "))
except ValueError:
print("Please enter a valid number of parking hours")
continue
if hours ‹= 0:
continue
print("Please enter a valid number of parking hours")
if hours ‹ 1:
fee = 0.08
elif vehicle_type == 1:
fee = 10 + (hours - 1) * 5
elif vehicle_type == 2:
fee = 30 + (hours - 1) * 15
print(f"Parking fee: {fee: 2f} THB")
summary-append ((vehicle_type, hours, fee))
cont = input("Do you want to continue? (y/n): ")-strip()-lower()
'--")
print("---
if cont != 'y':
break
print("VT Hours Cost")
total = 0
v for vtype, h,
f in summary:
print(f"(vtype} {h:.2f} {f:.2f}")
total += f
print(f"Total {total: .2f} THB*)