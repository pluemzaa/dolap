price = input("Enter product price ")
points = input("Enter your point:")
discount = min(points,500)
total = price-discount
print(f"discount:{discount:.2f}")
print(f"total :{total:.2f}Bath")