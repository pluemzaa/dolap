w = input("Enter your weight (kg):")
w = float(w)
h = input("Enter your height (m): ")
h = float(h)

Bmi = weight (kg) / (height(m))**2
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