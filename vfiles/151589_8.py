price = float(input("Enter product price:"))
point = int(input("Enter your point:"))
Discount = point/500 * point
total = price-Discount
print("Discount: {Discount%.2f} "% point)
print("total: {price%.2f} Baht"% total)