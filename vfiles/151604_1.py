price = float(input("Enter price:"))
point =  int(input("Enter Point"))
ds = 1/500 * point
print(f"Discount: {ds:.2f}")
total = price-ds
print(f"Total:{total:.2f} Bath")