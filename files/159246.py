w = float(input("Enter your weight (kg):"))
m = float(input("Enter your height (m):"))
if w >= 0 and m >= 0:
    bmi = float(w / m**2)
    print(f"Your BMI is: {bmi:.2f}" )
    if bmi < 18.5:
        print("Category: Underweight")
    elif bmi < 25:
        print("Category: Normal weight")
    elif bmi < 30 :
        print("Category: Overweight")
    else:
        print("Category: Obese")
else:
    print("Invalid input")