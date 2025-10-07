w = float(input("Enter your weight (kg): "))
H = float(input("Enter your height (m): "))
Bmical = w / (H**2)
    
if Bmical >= 0 :
    if Bmical <18.5 :
        print(f"Your BMI is: {Bmical:.2f}")
        print("Category: Underweight")
    elif Bmical >= 18.5 and Bmical < 25 :
        print(f"Your BMI is: {Bmical:.2f}")
        print("Category: Normal weight")
    elif Bmical >= 25  and Bmical < 30:
        print(f"Your BMI is: {Bmical:.2f}")
        print("Category: Overweight")
    else:
        print(f"Your BMI is: {Bmical:.2f}")
        print("Category: Obese")
else:
    print("Invalid input")