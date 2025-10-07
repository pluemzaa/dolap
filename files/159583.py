weight = float(input("Enter your weight (kg):"))
height = float(input("Enter your height (m):"))
BMI = weight  / (height)**2
if weight <=0 or height <=0 :
    print("Invalid input")
else:
    if  BMI < 18 :
        c=(" Underweight")
    elif BMI >=18 and BMI < 25 :
        c=(" Normal weight")
    elif BMI >=25 and BMI < 30 :
        c=(" Overweight")
    elif BMI >=30 :
        c=(" Obese")
    print(f"Your BMI is: {BMI:.2f}")
    print(f"Category:{c}")