w = float(input("Enter your weight (kg):"))
h = float(input("Enter your height (m):"))

BMI = w / (h**2)
if not ((w <= 0) or (h <= 0)) :
    print(f"Your BMI is: {BMI:.2f}")
    if BMI < 18.5:
        print("Category: Underweight")
    elif 18.5 <= BMI < 25:
        print("Category: Normal weight")
    elif 25 <= BMI < 30:
        print("Category: Overweight")
    else:
        print("Category: Obese")
else:
    print("Invalid input")