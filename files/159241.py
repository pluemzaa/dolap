weight = int(input(("Enter your weight (kg): ")))
height = float(input(("Enter your height (m): ")))
BMI = weight / (height**2)


if weight >=0 and height >=0 :
    if BMI < 18.5 :
        print(f"Your BMI is: {BMI:.2f} ") 
        print ("Category: Underweight")
    elif 18.5 <= BMI < 25 :
        print(f"Your BMI is: {BMI:.2f} ") 
        print ("Category: Normal weight")
    elif 25 <= BMI < 30 :
        print(f"Your BMI is: {BMI:.2f} ") 
        print ("Category: Overweight")
    else :
        print(f"Your BMI is: {BMI:.2f} ") 
        print ("Category: Obese")
else :
    print ("Invalid input")