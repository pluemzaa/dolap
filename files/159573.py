weight = 0
height = 0
BMI = 0

weight = float(input("Enter your weight (kg):"))
height = float(input("Enter your height (m):"))
BMI = weight /(height * height)
if BMI <= 0 :
    print("Invalid input")
else :
    print(f"Your BMI is: {BMI:.2f}")
    print("Category:",end='', flush=True)

    if BMI < 18.5 :
        print("Underweight")
    elif 18.5 <= BMI < 25 :
        print("Normal weight")
    elif 25 <= BMI < 30 :
        print("Overweight")
    elif BMI >= 30 :
        print("Obese")