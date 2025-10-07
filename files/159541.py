w = float(input("Enter your weight(kg): "))
h = float(input("Enter your height (m): "))
BMI = w/h**2
if w < 0:
    print("Invalid input")

elif BMI < 18.5:
    print(f"Your BMI is:{BMI:.2f}")
    print("category : Underweight")
elif 18.5 <= BMI < 25 :
    print(f"Your BMI is:{BMI:.2f}")
    print("category : Normal weight")
elif 25 <= BMI < 30 :
    print(f"Your BMI is:{BMI:.2f}")
    print("category : Overweight")
elif BMI >= 30 :
    print(f"Your BMI is:{BMI:.2f}")
    print("category : Obese")