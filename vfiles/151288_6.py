Produce_price = input("Enter produce price:")
Produce_price = float(Product_price)

Point = input("Enter your point:")
Point = int(Point)

Discount = 1/500 * Point
print("Discount: {:.2f}".format(Discount))

Total = Produce_price - Discount
print(f"Total: {Total:.2f} Bath")