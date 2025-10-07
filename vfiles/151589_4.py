price = float(input("Enter product price:"))
point = int(input("Enter your point:"))
Discount = 1/500 * point
total = price-Discount
print("discount: %.2f "% point)
print("total: %.2f Baht"% total)