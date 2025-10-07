price = float(input("Enter product price:"))
point = int(input("Enter your point:"))
ds = price/500
total =price-ds
print(f"Discount:{ds:.2f}")
print(f"Total: {total:.2f} Baht")