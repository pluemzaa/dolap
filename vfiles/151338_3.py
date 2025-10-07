price = float(input("Enter product price: "))
point = int(input("Enter your point: "))
point_f = 1/500 * point
print(f"Discount : {point_f:.2f} ")
Total = price - point_f
print(f"Total: {Total:.2f} Bath")