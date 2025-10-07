a = float(input("Enter your weight (kg):"))
b = float(input("Enter your height (m):"))

if a<0 or b<0:
    print("Invalid input")
else:
    BMI = a/b**2
    print(f"BMI: {BMI:.2f}")
if BMI < 18.5:
    print("Category: Underweight")
elif BMI < 25:
    print("Category: Normal weight")
elif BMI < 30:
    print("Category: Overweight")
else:
    print("Category: Obese")