price = input("Enter product price:") 
point = input("Enter your point:") 
price = float(price)
point = int(point)
Discount = 1/500*point
total = price - point

print("Discount: ""%.2f" % Discount)
print("Total: ""%.2f" % total)