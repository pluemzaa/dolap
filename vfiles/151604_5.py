price = float(input("Enter price:"))
point = int(input("Enter Point:"))
ds = point/500 
print(f"Discount:{ds:.2f}")
total = price-ds
print(f"Total:{total:.2f}Bath")