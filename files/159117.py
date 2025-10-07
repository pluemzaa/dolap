x = float(input("Enter your weight (kg):"))
y = float(input("Enter your height (m):"))

if x > 0 and y > 0:
    bmi = x / (y**2)
    print (f"Your BMI is: {bmi:.2f}")
    if bmi < 18.5:
        print("Category: Underweight")
    elif bmi >= 18.5 and  bmi < 25:
        print("Category: Normal weight")
    elif bmi >= 25 and  bmi < 30:
        print("Category: Overweight")
    elif bmi >= 30:
        print("Category:Obese")
    
        
else:
    print("Invalid input")