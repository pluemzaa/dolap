price = float(input("Enter product price: "))
point = int(input("Enter your point: "))
discount = 1/500*point
print("Discount: %.2f",%(discount))
total = price - discount
print(f"Total: {total:.2f} Haht")