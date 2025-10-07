price = (input("Enter product price: "))
float(price)
point =(input("Enter your point: "))
int(point)
discount = 1/500 * point
print(f"Discount: {discount:.2f}")
total = price-discount
print (f"Total: {total:.2f} Bath")