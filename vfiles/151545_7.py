price = float(input("Enter product price:"))
point = int(input("Enter your point:"))
Discount =  1/500 * point
total = price-Discount
print("Discount: %.2f "% point)
print("Total: %.2f Baht"% total)