price = input("Enter product price: ")
price = float(price)
point = 1/500 * price
discount =  input("Enter your point: ")
discount = float(discount)
point = 1/500 * discount
print("%.2f bath = %.2f points"%(price,point))
print(f"{price:.2f} bath = {point: .2f} Total: 1220.10")