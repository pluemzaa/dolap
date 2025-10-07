weight = int(input("Enter your weight (kg): "))
height = float(input("Enter your height (m): "))

BMI = weight / (height**2)

if weight >= 0 and height >=0 :
    if BMI < 18.5 :
        print ("Your BMI is: %.2f" %BMI)
        print ("Category: Underweight")
    elif BMI <= 25 :
        print ("Your BMI is: %.2f" %BMI)
        print ("Category: Normal weight")
    elif BMI <= 30 :
        print ("Your BMI is: %.2f" %BMI)
        print ("Category: Overweight")
    else :
        print ("Your BMI is: %.2f" %BMI)
        print ("Category: Obese")
else :
    print ("Invalid input")