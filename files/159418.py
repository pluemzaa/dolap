w = float(input("Enter your weight (kg): "))
h = float(input("Enter your height (m): "))
BMI = w/h**2
if w <= 0 and h <= 0:
    print("Invalid input")
else:
    print("Your Bmi is: %.2f" % BMI)
    if BMI < 18.5:
        print("Category: Under weight")
    if 18.5 <= BMI < 25:
        print("Category: Normal weight")
    if 25 <= BMI < 30:
        print("Category: Overweight")
    if BMI >= 30:
        print("Category: Obese")