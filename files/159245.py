kg = int(input("Enter your weight (kg): "))
m = float(input("Enter your height (m): "))
BMI = float
BMI = kg / m**2
if kg > 0 and m > 0 :
    if BMI < 18.5 :
        print ("Your BMI is: %.2f" %BMI)
        print ("Category: Underweight")
    elif BMI < 25 :
        print ("Your BMI is: %.2f" %BMI)
        print ("Category: Normal weight")
    elif BMI < 30:
        print ("Your BMI is: %.2f" %BMI)
        print ("Category: Overweight")
    else :
        print ("Your BMI is: %.2f" %BMI)
        print ("Category: Obese")
else :
    print ("Invalid input")