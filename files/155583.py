price = float(input("Enter product price: "))
point = int(input("Enter your point: "))

Discount = point / 500

if Discount > price :
    Discount = price
total = price - Discount

pi = 3.14159
print(f"Discount {pi:.2f}")
print("Total: %.2f Baht" % total)