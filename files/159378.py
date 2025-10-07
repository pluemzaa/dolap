Weight = int(input("Enter your weight (kg):"))
Height = float(input("Enter your height (m): "))
if Weight <= 0:
    print("Invalid input ")
elif Height <= 0:
    print("Invalid input ")
if Weight > 0 and Height > 0:
     Bmi = Weight / (Height * Height)
     print(f"Your BMI is: {Bmi:.2f}")
     if Bmi < 18.5:
         print("Category: Underweight ")
     elif Bmi >= 18.5 and Bmi < 25:
         print("Category: Normal weight ")
     elif Bmi >= 25 and Bmi < 30:
         print("Category: Overweight ")
     else:
         print("Category: Obese ")