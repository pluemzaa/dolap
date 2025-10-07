price =float(input("Enter product price:"))
point =float(input("Enter your point: "))
ds = point/500
print(f"Discount: {ds:.2f}")
total =price-ds
print(f"Total:{total:.2f}ฺ Baht")