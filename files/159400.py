w = float(input("Enter your weight(kg):"))
h = float(input("Enter your height(m):"))

if w <= 0:
    print("Invalid input")
if h <= 0:
    print("Invalid input")
    
BMI = w/(h**2)
print("Your BMI is:%.2f" % BMI)
if   BMI < 18.5:
        print("Category: Under weight")
elif   18.5 <= BMI < 25:
        print("Category: Normal weight")
elif   25 <= BMI < 30:
        print("Category: Overweight")
else:
        print("Category: Obese")