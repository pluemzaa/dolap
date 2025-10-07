weight = float(input("Enter your weight (kg): "))
height = float(input("Enter your height (m): "))

if weight <= 0 or height <= 0:
    print("Invalid input")
    exit()

bmi = weight / (height ** 2)
print(f"Your BMI is: {bmi:.2f}")

if bmi < 18.5:
    category = "Underweight"
elif bmi < 25:
    category = "Normal weight"
elif bmi < 30:
    category = "Overweight"
else:
    category = "Obese"

print(f"Category: {category}")