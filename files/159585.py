w = float(input("Enter your weight (kg): "))
h = float(input("Enter your height (m): "))
if w <=0 or h <= 0:
            print("Invalid input")
else:
    bmi = w/h**2
    print("Your BMI is: ","%.2f"%bmi)
    if bmi >=18.5 and bmi <25 :
        print("Category: Normal weight")
    else:
        if bmi >=25 and bmi <30 :
            print("Category: Overweight")
        elif bmi >=30 :
            print("Category: Obese")
        elif bmi <18.5 :
            print("Category: Underweight")