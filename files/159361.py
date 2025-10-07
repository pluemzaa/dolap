w = float(input("Enter your weight (kg): "))
h = float(input("Enter your height (m): "))

if w <= 0 or h <= 0:
    print("Invalid input")
else:
    bmi = w/h**2
    print("Your BMI is: %.2f" %bmi)
    print("Category: ", end='')
    if bmi < 18.5:
        print("Underweight")
    elif bmi < 25:
        print("Normal weight")
    elif bmi < 30:
        print("Overweight")
    else:
        print("Obese")