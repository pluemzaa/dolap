w = int(input("Enter your weight (kg):"))
h = float(input("Enter your height (m):"))
if w <= 0 :
    print("Invalid input")
else:
    bmi = (w)/(h)**2
    print(f"Your BMI is: {bmi:.2f}")
    if bmi < 18.5 :
        print("Category: Underweight")
    if 18.5 <= bmi < 25 :
        print("Category: Normal weight")
    if 25 <= bmi < 30 :
        print("Category: Overweight")
    if bmi >= 30 : 
        print("Category: Obese")