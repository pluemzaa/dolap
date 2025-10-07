w =float(input("Enter your weight (kg):"))
h =float(input("Enter your height (m):"))
BMI= w/h**2

if w <=0:
    print("Invalid input")
else:
    print("Your BMI is:",'%.2f'% BMI)
    if BMI < 18.5:
        print("Category:Underweight")
    elif BMI < 25:
        print("Category:Normal weight")
    elif BMI < 30:
        print("Category:Overweight")
    else:
        print("Category:Obese")