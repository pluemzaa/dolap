wei = float(input("Enter your weight (kg): "))
hei = float(input("Enter your height (m): "))
BMI = wei / (hei ** 2)

if wei <= 0 or hei <=0:
      print("Invalid input")
elif BMI < 18.5:
      print(f"Your BMI is: {BMI:.2f}")
      print("Category: Underweight")
elif 18.5 <= BMI < 25 :
      print(f"Your BMI is: {BMI:.2f}")
      print("Category: Normal weight")
elif 25 <= BMI < 30 :
      print(f"Your BMI is: {BMI:.2f}")
      print("Category: Overweight")
elif BMI >= 30 :
      print(f"Your BMI is: {BMI:.2f}")
      print("Category: Obese")