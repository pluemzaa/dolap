wg = float(input("Enter your weight (kg): "))
he = float(input("Enter your height (m): "))

if wg > 0 and he > 0 :
    BMI =  wg / (he**2)
    print(f"Your BMI is: {BMI:.2f}")
        
    if BMI < 18.5 :
        print("Category: Underweight")
    elif BMI < 25:
        print("Category: Normal weight")
    elif BMI < 30:       
        print("Category: Overweight")
    else:
        print("Category: Obese")
else:
    print("Invalid input")