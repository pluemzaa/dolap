price = 1250.50
point = int(input("Enter your point:"))
Discount = 1/500*point
print(f"{Discount:.2f}")
Total = price - Discount
print(f"{Total:.2f}")