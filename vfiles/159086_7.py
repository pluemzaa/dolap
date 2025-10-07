weight = float(input("Enter your weight(kg): "))

height = float(input("Enter your height(m): "))
BMI = weight / (height)**2
print(f"Your BMI is : {BMI:.2f}")
if weight <=0 and height <= 0:
    if BMI < 18.5:
        print("Underweight")
    elif BMI >= 18.5 and Bmi < 25:
        print("Normal weight")
    elif BMI >= 25 and Bmi < 30:
        print("Overweight")
    elif BMI >= 30:
        print("Obese")
    else:
        print("invalid input")