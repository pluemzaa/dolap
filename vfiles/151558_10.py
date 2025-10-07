epp=float(input("Enter product price:"))
eyp=int(input("Enter your point:"))
ds= eyp/500
print(f"Discount:{ds:.2f}")
tt=epp-ds
print(f"Total:{tt:.2f} Baht")