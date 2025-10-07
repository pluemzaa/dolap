w = float(input("Enter your weight (kg): "))
h = float(input("Enter your height (m): "))

if w > 0 and h > 0:
    b = w/h**2
    print(f"Your BMI is: {b:.2f}")
    if b < 18.5:
        print("Category: Underweight")
    elif b < 25:
        print("Category: Normal weight")
    elif b < 30:
        print("Category: Overweight")
    else:
        print("Category: Obese")  
else:
    print("Invalid input")