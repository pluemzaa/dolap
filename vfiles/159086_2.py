Bmi = input("Enter your weight (kg):")
Bmi = input("Enter your height (m): ")
weight = 1
height = 1
Bmi = weight  / (height)**2
if Bmi < 18.5:
    print("Underweight")
    if Bmi >= 18.5 and Bmi < 25:
        print("Normal weight")
    elif Bmi >= 25 and Bmi < 30:
        print("Overweight")
    else:
        print("Obese")
        print(f"Your Bmi is : {Bmi:.2f}")
else:
    print("invalid input")