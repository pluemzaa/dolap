W = int(input("Enter your weight (kg):"))
H = float(input("Enter your height (m):"))
if W <=0:
    print("Invalid input")
elif H <=0:
    print("Invalid input")
if W > 0 and H > 0:
    BMI = W/(H*H)
    print(f"Your BMI is:{BMI:.2f}")
    if BMI < 18.5:
        print("Category:Underweight")
    elif BMI >= 18.5 and BMI < 25:
        print("Category:Normal weight")
    elif BMI >= 25 and BMI < 30:
        print("Category:Overweight")
    else:
        print("Category:Obese")