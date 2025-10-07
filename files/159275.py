w = float(input("Enter your weight (kg): "))
h = float(input("Enter your height (m): "))
bmi = w / h**2
if w > 0 and h > 0:
    print(f"Your BMI is: {bmi:.2f}")
    if bmi < 18.5:   
        print("Category: Underweight")
    elif 18.5 <= bmi and bmi < 25: 
        print("Category: Normal weight")
    elif 25 <= bmi and bmi < 30: 
        print("Category: Overweight")
    else:
        print("Category: Obese")
else:
    print("Invalid input")