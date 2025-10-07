kg = float(input("Enter your weight (kg):"))
m = float(input("Enter your height (m):"))
BMI = kg / (m)**2
BMI = float(BMI)
if kg >0 and m > 0:
    print(f"Your BMI is: {BMI:.2f}")
    if BMI < 18.5:
        print("Category: Underweight")
    if BMI >= 18.5 and BMI < 25:
        print("Category: Normal weight") 
    if BMI >= 25 and BMI < 30:
        print("Category: Overweight")
    if BMI >= 30:
        print("Category: Obese")           
else:
    print("Invalid input")