total = 0
discount = 0
print("Enter price")
price = float(input())
print("Enter point")
point = int(input())
discount = float(point) / 500
total = price - discount
print("Total: " + str(total) + "Baht")