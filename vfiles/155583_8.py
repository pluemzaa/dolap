price = float(input("Enter product price: "))
point = int(input("Enter your point: "))

Discount = point / 500

if Discount > price :
    Discount = price
total = price - Discount
    
print("Discount %.2f" % Discount)
print("Total: %.2f Baht" % total)

pi = 3.14159
print(f"Discount {pi:.2f}")