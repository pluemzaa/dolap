weight = int(input("Enter your weight (kg):"))
height = float(input("Enter your height (m):"))
if weight <= 0 :
    print("Invalid input")
else:
    BMI = (weight)/(height)**2
    print(f"Your BMI is: {BMI:.2f}")
    if BMI < 18.5 :
        print("Category: Underweight")
    if 18.5 <= BMI < 25 :
        print("Category: Normal weight")
    if 25 <= BMI < 30 :
        print("Category: Overweight")
    if BMI >= 30 :
        print("Category: Obese")