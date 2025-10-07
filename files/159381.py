# BMI < 18.5 → Underweight
# 18.5 ≤ BMI < 25 → Normal weight
# 25 ≤ BMI < 30 → Overweight
# BMI ≥ 30 → Obese

w = float(input("Enter your weight (kg): "))
h = float(input("Enter your height (m): "))
bmi = w / (h)**2
if bmi > 0:
    print (f"Your BMI is: {bmi:.2f}")
    if bmi < 18.5:
        print("Category: Underweight")
    elif bmi < 25:
        print("Category: Normal weight")
    elif bmi < 30:
        print("Category: Overweight")
    else:
        print("Category: Obese")
else:
    print("Invalid input")