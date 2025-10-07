price = int(input("Enter product price" ))
price = int(input("Enter your point"))
price = float(price)
ponit = 1/500 * price 
Discount = ponit/500
Total = price -Discount
print(Discount)
print(Total)
print("Discount%.2f ,  Totalt: %.2f Baht" % (Discount,Total))
print(f"price rounded to 2 decimals: {price:.2f}")