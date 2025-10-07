Bmi = float(input("Enter your weight (kg):"))
Bmi = float(input("Enter your height (m): "))

Bmi = weight(kg) / (height(m))2
if Bmi < 18.5:
    print("Underweight")
elif Bmi >= 18.5 and Bmi < 25:
    print("Normal weight")
elif Bmi >= 25 and Bmi < 30:
    print("Overweight")
else:
    print("Obese")
    print("Your Bmi is : {Bmi:.2f}")