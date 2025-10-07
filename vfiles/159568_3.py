weight = float(input("Enter your weight (kg):"))
height = float(input("Enter your height (m):"))

BMI = weight/(height**2)
if BMI <= 0 :
        print("Invalid temp.")
else:
    if BMI < 18.5 :
        print (f"Your BMI is:{BMI:.2F}")
        print("Category: Underweight")
    elif 18.5 <= BMI < 25 :
        print (f"Your BMI is:{BMI:.2F}")
        print("Category: Normal weight")
    elif 25 <= BMI < 30  :
        print (f"Your BMI is:{BMI:.2F}")
        print("Category: Overweight")
    else :
        print (f"Your BMI is:{BMI:.2F}")
        print("Category: Obese")