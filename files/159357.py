w = float(input("Enter your weight (kg):"))
h = float(input("Enter your height (m):"))
b = w/(h**2)
if b > 0:
    if b < 18.5:
        print(f"Your BMI is:{b:.2f}")
        print("Category:Underweight")
    elif b < 25:
        print(f"Your BMI is:{b:.2f}")
        print("Category:Normal weight")
    elif b < 30:
        print(f"Your BMI is:{b:.2f}")
        print("Category:Overweight")
    else:
        print(f"Your BMI is:{b:.2f}")
        print("Category:Obese")
else:
    print("Invalid input")