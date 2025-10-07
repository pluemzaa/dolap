weight = float(input("Enter your weight (kg): "))
height = float(input("Enter your height (m): "))
bmi = weight / height**2
if weight >= 0 and height >= 0:  
    if weight > 0  and height > 0:
        if bmi < 18.5:
            print(f"Your BMI is: {bmi:.2f}")
            print("Category: Underweight")
        if 18.5 <= bmi < 25:
            print(f"Your BMI is: {bmi:.2f}")
            print("Category: Normal weight")
        elif 25 <= bmi < 30:
            print(f"Your BMI is: {bmi:.2f}")
            print("Category: Overweight")
        elif bmi >= 30:
            print(f"Your BMI is: {bmi:.2f}")
            print("Category: Obese")
print("Invalid input")