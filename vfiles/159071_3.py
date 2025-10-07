BMI = float(input("Enter your weight (kg): "))
H = int(input("Enter your height (m):"))
if BMI > 0 :
    if BMI < 18.5 :
        print("Category:Underweight")
    elif BMI <=18.5 and < 25 :
        print("Category:Normal weight")
    elif BMI <=25  and < 30  :
        print("Category:Overweight")
    elif BMI >= 30   :
        print("Category:Obese")
else:
    print("Invalid input")
Bmical = BMI /H*2
print("Your BMI is:" ,Bmical)