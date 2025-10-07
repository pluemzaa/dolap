w = float(input("Enter your weight (kg):"))
h = float(input("Enter your height (m):"))

BMI = w / h ** 2
Cate = ""

if BMI < 18.5:
     Cate = "Underweight"
elif BMI < 25:
     Cate = "Normal weight"
elif BMI < 30:
     Cate = "Overweight"
else:
     Cate = "Obese"

if w > 0 and h > 0:
    print(f"Your BMI is: {BMI:.2f}")
    print("Category:",Cate)
else:
    print("Invalid input ")