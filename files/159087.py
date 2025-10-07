w = float(input("Enter your weight (kg): "))
h = float(input("Enter your height (m): "))
bmi = w / h**2

if w >= 0 and h >= 0:
    if w>0 and h > 0:
        if bmi < 18.5:
          print(("Your BMI is:%.2f"%bmi))
          print("Category: Underweight")
        elif bmi >=18.5 and bmi<= 25 :
          print(("Your BMI is:%.2f"%bmi))
          print("Category: Normal weight")
        elif bmi >= 25 and bmi < 30 :
          print(("Your BMI is:%.2f"%bmi))
          print("Category: Overweight")
        elif bmi >= 30:
          print(("Your BMI is:%.2f"%bmi))
          print("Category: Obese")
print("Invalid input")