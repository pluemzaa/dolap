price = input("Enter product price: ")
price = float(price)
point = 1/500 * price
discount = input("Enter your point: ")
discount = float(discount)
discount = 1/500 * discount
total = float(discount)
total = 1/500*total
print("%.2f bath = %.2f points"%(price,point))
print(f"{price:.2f} bath = {point: .2f} point=")
print("%.2f discount = %.2f total"%(point,discount))
print(f"{price:.2f} total = {discount: .2f} discount=")
print(f"Pi rounded to 2 discount: {point:.2f}")
print("%.2f bath = %.2f total"%(discount,total))