price = float(input("Enter product price: "))
point = int(input("Enter your point: "))

discount = 2 / 500

if discount > price :
    discount = price
total = price - discount
    
print("discount %.2f" % discount)
print("Total: %.2f Baht" % total)