weight = float(input("Enter your weight (kg):"))
height = float(input("Enter your height (m):"))
bmi = weight / (height)**2
if weight <= 0 or height <= 0:
    print("Invalid input") 
else:
    if bmi < 18.5:
        p=( "Underweight") 
    if bmi >= 18.5 and bmi < 25:
        p=("Normal weight")  
    if bmi >= 25 and bmi < 30:
        p=("Overweight")       
    if bmi >= 30:
        p=("Obese")
    print(f"Your BMI is: {bmi :.2f}")
    print(f"Category:{p}")