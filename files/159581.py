kg = float(input("Enter your weight (kg): "))
m = float(input("Enter your height (m): "))
BMI = kg/(m**2)
if BMI > 0 :
    print(f'Your BMI is: {BMI:.2f}')
    if BMI < 18.5:
        print("Category: Underweight")
    elif 18.5 <= BMI < 25:
        print("Category: Normal weight")
    elif 25 <= BMI < 30:
        print("Category: Overweight")
    elif BMI >= 30:
        print("Category: Obese")
else :
    print("Invalid input")