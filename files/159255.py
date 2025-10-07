weight = float(input("Enter your weight (kg):"))
height = float(input("Enter your height (m):"))
Category = ''
BMI = 0

if weight <= 0 or height <= 0:
        print("Invalid input")
else:
        BMI = weight / (height * height)
        if BMI < 18.5:
            Category =  ('Underweight')
        elif 18.5 <= BMI < 25 :
            Category =  ('Normal weight')
        elif 25 <= BMI < 30 :
            Category =  ('Overweight')
        else:
            Category =  ('Obese')
        print(f"Your BMI is : {BMI:.2f}")
        print(f"Category: {Category}")