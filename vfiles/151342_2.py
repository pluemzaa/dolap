price = input("Enter product price: ")
point = int(input("Enter your point: "))
price = float(price)
discont = point/500 
total = point - price
print(f"Discount: {discont:.2f}" )
print(f"Total = {total:.2f} baht" )