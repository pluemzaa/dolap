price = float(input("Enter product price: " ))
point = int(input("Enter your point: "))

Discount = point/500
Total = price - Discount

print("Discount:%.2f"  %Discount)
print("Totalt: %.2f Baht" % Total)