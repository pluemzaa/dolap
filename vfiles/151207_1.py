Product_price = input("Enter product price:")
Product_price = float(Product_price)

Point = input("Enter your point:")
Point = int(Point)

Discount = 1/500 * Point 
print("Discount: {:.2f}".format(Discount))

Total = Product_price - Discount
print(f"Total: {Total:.2f} Baht")