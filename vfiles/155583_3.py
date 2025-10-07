price = float(input("Enter product price: "))
point = int(input("Enter your point: "))

Discount = 2 / 500

if Discount > price :
    Discount = price
total = price - Discount
    
print("Discount %.2f" % Discount)
print("Total: %.2f Baht" % total)