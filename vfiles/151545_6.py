price = float(input("Enter product price:"))
point = int(input("Enter your point:"))
Discounct =  1/500 * point
total = price-Discounct
print("Discounct: %.2f "% point)
print("Total: %.2f Baht"% total)