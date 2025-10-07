weight = float(input("Enter your weight (kg):"))
height = float(input("Enter your height (m):"))

if weight <= 0 or height <= 0:
    print("Invalid input")    

BMI = weight/(height)**2

print(f"Your BMI is:{BMI:.2f}")

if BMI < 18.5:
    print("Category: Underweight")

elif BMI >= 18.5 and BMI < 25:
    print("Category: Normal weight") 

elif BMI >= 25 and BMI < 30:
    print("Category: Overweight")

if BMI >= 30:
    print("Category: Obese")