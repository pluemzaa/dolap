w = input("Enter your weight(kg): ")
w = float(w)
h = input("Enter your height(m): ")
h = float(h)

Bmi = w / h**2 
if Bmi < 18.5:
    print("Underweight")
    if Bmi >= 18.5 and Bmi < 25:
        print("Normal weight")
    elif Bmi >= 25 and Bmi < 30:
        print("Overweight")
    elif Bmi >= 30:
        print("Obese")
    else:
        print("invalid input")
else:
    print(f"Your Bmi is : {Bmi:.2f}")