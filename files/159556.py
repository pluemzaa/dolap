w = float(input("Enter your weight (kg): "))
h = float(input("Enter your height (m): "))
BMI = w / (h**2)
if BMI <=0 :
    print("Invalid input")
else:
    print(f"Your BMI is: {BMI:.2f}")
    print("Category: ",end='',flush=True)
    if BMI < 18.5:
        print("Underweight")
    elif 18.5 <= BMI < 25 :
        print("Normal weight")
    elif 25 <= BMI < 30 :
        print("Overweight")
    else:
        if BMI >= 30:
         print("Obese")