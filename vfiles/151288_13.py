price = input("Enter produce price: ")
price = float(price)
Point = input("Enter your point: ")
Point = int(Point)
Discount = 1/500 * Point
print(f"Discount:{Discount:.2f} ")
Total = price - Discount
print(f"Total: {Total:.2f} Bath ")