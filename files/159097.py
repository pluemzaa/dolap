w = float(input("Enter your weight (kg): "))
h = float(input("Enter your height (m): "))
bmi = w/(h**2)

if bmi > 0 and bmi < 18.5: 
    print("Your BMI is: %.2f"% (bmi))
    print("Category: Underweight")
if bmi >= 18.5 and bmi < 25:
    print("Your BMI is: %.2f"% (bmi))
    print("Category: Normal weight")
elif bmi >= 25 and bmi < 30:
    print("Your BMI is: %.2f"% (bmi))
    print("Category: Overweight")
elif bmi >= 30 :
    print("Your BMI is: %.2f"% (bmi))
    print("Category: Obese")
else:
    print("Invalid input")