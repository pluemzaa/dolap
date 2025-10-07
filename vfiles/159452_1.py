W = int(input("Enter your weight (kg): "))
H = float(input("Enter your height (m): "))
BMI = float((W)/(((H)**2)))
if  W <= 0 and H <= 0:
    if BMI <= 18.5:
        print("Category: Underweight")
        print((f"Your BMI is: {BMI}"))
    if 18.5<=BMI< 25:
        print("Category: Normal weight")
        print((f"Your BMI is: {BMI}"))
    if 25 <= BMI < 30:
        print("Category: Mild fever")
        print((f"Your BMI is: {BMI}"))
    if BMI >= 30:
        print("Category: Obese")
        print((f"Your BMI is: {BMI}"))
else:
    print("Invalid input")