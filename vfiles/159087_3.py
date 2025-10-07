w = float(input("Enter your weight (kg): "))
h = float(input("Enter your height (m): "))
bmi = w / h**2

if bmi >= 0:
    print(("Your BMI is: %.2f"%bmi))
    if bmi < 18.5:
        print("Category: Underweight")
    elif bmi >=18.5 and bmi<= 25 :
        print("Category: Normal weight")
    elif bmi >= 25 and bmi < 30 :
        print("Category: Overweight")
    elif bmi >= 30:
        print("Category: Obese")
else:
    print("Invaild input")