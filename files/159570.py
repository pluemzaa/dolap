w = int(input("Enter your weight (kg):"))
h = float(input("Enter your height (m):"))
BMI = float(w / (h**2))
a = "Category:"
if BMI <= 0:
    print("Invalid input")
else:
    BMI = float(w / (h**2))
    print(f"Your BMI is: {BMI:.2f}")
    if BMI < 18.5:
        print(a,"Underweight")
    elif BMI > 18.5 and BMI < 25:
        print(a,"Normal weight")
    elif BMI > 25 and BMI < 30:
        print(a,"Overweight")
    elif BMI > 30:
        print(a,"Obese")