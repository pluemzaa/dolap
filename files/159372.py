w = float(input("Enter your weight (kg):"))
h = float(input("Enter your height (m):"))

total = w/h**2
if w > 0 and h > 0:
    print("Your BMI is: %.2f" % total)
    if total < 18.5:
        print("Category: Underweight")
    if 18.5 <= total < 25:
        print("Category: Normal weight")
    if 25 <= total < 30:
        print("Category: Overweight")
    if total >= 30:
        print("Category: Obese")
else:
    print("Invalid input")