price = input('Enter product price: ')
point = input('Enter your point: ')

price = float(price)
point = int(point)

discount = 1/500 * point
print(f"Discount: {discount.2f}")
Total = price-discount
print(f"Total: {Total:.2f}")