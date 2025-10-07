weight=float(input("Enter your weight (kg):"))
height=float(input("Enter your height (m):"))
BMI = 0
if weight <=0 or height <=0:
    print("Invalid input") 
else:
    BMI= weight/(height)**2
    print(f"Your BMI is: {BMI:.2f}")
if BMI < 18.5:
    print("Category: Underweight")
elif 18.5 < BMI < 25:
    print("Category: Normal weight")
elif 25 < BMI < 30:
    print("Category: Overweight")
elif BMI > 30:
    print("Category: Obese") 
else:
    print("Invalid input")