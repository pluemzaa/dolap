a = float(input("Enter product price: "))
b = int(input("Enter your point: "))
#500แต้มเท่ากับ1บาท
c = b/500
d = a-c
print(f"Discount: {c:.2f}")
print(f"Total: {d:.2f} Baht")