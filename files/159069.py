w = float(input("Enter your weight (kg):"))
h = float(input("Enter your height (m):"))

BMI = w/(h**2)
if BMI >= 0:
    if BMI<18.5:
        bmi_s = "Underweight"
    elif BMI<25:
        bmi_s = "Normal weight"
    elif BMI<30:
        bmi_s = "Overweight"    
    else:
        bmi_s = "Obese"
    print(f"Your BMI is:{BMI:.2f}")
    print(f"Category:{bmi_s}")
else:
    print("Invalid input")