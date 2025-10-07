w = float(input("Enter your weight (kg):"))
h = float(input("Enter your height (m):"))
bmi = w/(h**2)
if w <= 0 or h <= 0:
    print("Invalid input")
elif bmi < 18.5 :
    print(f"Your BMI is: {bmi:.2f}")
    print("Category:Underweight")
elif 18.5 <= bmi and bmi < 25:
    print(f"Your BMI is: {bmi:.2f}")
    print("Category:Normal weight")
elif 25 <= bmi and bmi < 30:
    print(f"Your BMI is: {bmi:.2f}")
    print("Category:Overweight")
else :
    print(f"Your BMI is: {bmi:.2f}")
    print("Category:Obese")