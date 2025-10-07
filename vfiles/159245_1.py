kg = int(input("Enter your weight (kg): "))
m = float(input("Enter your height (m): "))
BMI = (kg / m) ** 2
if kg > 0 and m > 0 :
    if BMI < 18.5 :
        print ("Underweight") 
    elif BMI < 25 :
        print ("Normal weight")
    elif BMI < 30:
        print ("Overweight")
    else :
        print ("Obese")
else :
    print ("Invalid input")