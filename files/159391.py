w = float(input("Enter your weight (kg):"))
h = float(input("Enter your height (m):"))

if w <= 0:
    print("Invalid input")
if h <= 0:
    print("Invalid input")

bmi = w/(h**2)
print("Your BMI is:%.2f" % bmi)
if bmi < 18.5:
    print("Category: Underweight")
elif 18.5 <= bmi < 25:
    print("Category: Normal weight")
elif 25 <= bmi < 30:
    print("Category: Overweight")
else:
    print("Category: Obese")