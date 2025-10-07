we = float(input("Enter your weight (kg): "))
he = float(input("Enter your height (m): "))
bmi = we/(he**2)
if bmi >= 0:
    if bmi < 18.5:
        print("Your BMI is: %.2f" % bmi)
        print("Category: Underweight")
    elif bmi >= 18.5 and bmi < 25:
        print("Your BMI is: %.2f" % bmi)
        print("Category: Normal weight")
    elif bmi >= 25 and bmi < 30:
        print("Your BMI is: %.2f" % bmi)
        print("Category: Overweight")
    else:
        print("Your BMI is: %.2f" % bmi)
        print("Category: Obese")
else :
    print("Invalid input")