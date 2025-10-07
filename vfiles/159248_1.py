w = float(input("Enter your weight (kg):"))
h = float(input("Enter your height (m):"))

if h > 0 and w > 0:
    BMI = w / (h ** 2)
    if BMI < 18.5:
        print("Category: Underweight")
    elif BMI >= 18.5 and BMI < 25:
        print("Category: Normal weight")
    elif BMI >= 25 and BMI < 30:
        print("Category: Overweight")  
    elif BMI > 30:
        print("Category: Obese")
else:
    print("Invalid input")