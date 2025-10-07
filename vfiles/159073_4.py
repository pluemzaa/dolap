W = float(input("Enter your weight (kg): "))
H = float(input("Enter your height (m): "))

if W > 0 and H >0:  
    BMI = W/(H**2)
    print(f"Your BMI is: {BMI:.2f}")
        
    if BMI < 18.5:
        print("Category: Underweight")
    elif BMI < 25:
        print("Category: Normal weight")
    elif BMI < 30:
        print("Category: Overweight")
    else:
        print("Category: Obese")
else:
    print("Invalid input")