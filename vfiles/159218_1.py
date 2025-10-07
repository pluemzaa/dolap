W =int(input("Enter your weight (kg):"))
H = float(input("Enter your height (m):"))

if W and H > 0:
    BMI = W / H**2
    print(f"Your BMI is: {BMI:.2f}")
    if BMI < 18.5:
        print("Category: Under weight")
    elif 18.5 <= BMI < 25:
        print("Category: Normal weight")
    elif 25 <= BMI < 30:
        print("Category: Over weight")
    else:
        print("Category: Obese")
else:
    print("Invalid input")